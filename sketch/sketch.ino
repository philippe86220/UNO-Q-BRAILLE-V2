#include <Arduino.h>
#include <Arduino_RouterBridge.h>

extern "C" void matrixWrite(const uint32_t *buf);
extern "C" void matrixBegin();

const int MATRIX_WIDTH  = 13;
const int MATRIX_HEIGHT = 8;

String setBrailleDual(int prefixMask, int charMask);
void clearFrame(uint32_t frame[4]);
void setPixelBit(uint32_t frame[4], int x, int y);
void drawBrailleCell(uint32_t frame[4], uint8_t mask, int xOffset);
void showBraille(uint8_t prefixMask, uint8_t charMask);

int allOnBraille(int dummy);
int allOffBraille(int dummy);

void setup() {
  Bridge.begin();
  matrixBegin();

 
  Bridge.provide("allOnBraille", allOnBraille);
  Bridge.provide("allOffBraille", allOffBraille);
  Bridge.provide("setBrailleDual", setBrailleDual);
}

void loop() {
  delay(10);
}


int allOnBraille(int dummy) {
  (void)dummy;
  showBraille(63, 63);
  return 63;
}

int allOffBraille(int dummy) {
  (void)dummy;
  showBraille(0, 0);
  return 0;
}

void clearFrame(uint32_t frame[4]) {
  frame[0] = 0;
  frame[1] = 0;
  frame[2] = 0;
  frame[3] = 0;
}


void setPixelBit(uint32_t frame[4], int x, int y) {
  if (x < 0 || x >= MATRIX_WIDTH) return;
  if (y < 0 || y >= MATRIX_HEIGHT) return;

  int index = y * MATRIX_WIDTH + x;
  int word  = index / 32;
  int bit   = index % 32;

  frame[word] |= (1u << bit);
}

void drawBrailleCell(uint32_t frame[4], uint8_t mask, int xOffset)
{
    int xs[2] = {xOffset, xOffset + 1};
    int ys[3] = {1,3,5};

    for (int i = 0; i < 6; i++) {
        if (mask & (1 << i)) {

            int col = (i >= 3);
            int row = i % 3;

            int x = xs[col];
            int y = ys[row];

            setPixelBit(frame, x, y);
        }
    }
}

void showBraille(uint8_t prefixMask, uint8_t charMask)
{
    uint32_t frame[4];
    frame[0] = frame[1] = frame[2] = frame[3] = 0;

    if(prefixMask)
        drawBrailleCell(frame, prefixMask, 1);

    drawBrailleCell(frame, charMask, 5);

    matrixWrite(frame);
}

String setBrailleDual(int prefixMask, int charMask)
{
    showBraille(prefixMask, charMask);
    return "OK";
}
