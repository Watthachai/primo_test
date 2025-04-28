# Merge Sorted Arrays (TypeScript)

โปรเจกต์นี้เป็นฟังก์ชัน TypeScript ที่รวม (merge) อาร์เรย์จำนวนเต็มสามชุดเข้าด้วยกันให้เป็นอาร์เรย์เดียวที่เรียงลำดับจากน้อยไปมาก (ascending) โดยไม่ใช้ `.sort()`

## 🌟 คุณสมบัติหลัก

- รวมอาร์เรย์ตัวเลข 3 ชุด (`collection_1`, `collection_2`, `collection_3`)
- จัดการกับ `collection_2` ที่เรียงลำดับจากมากไปหาน้อย (descending)
- คืนค่าเป็นอาร์เรย์ใหม่ที่เรียงลำดับจากน้อยไปหามาก
- ไม่ใช้ `Array.prototype.sort()`
- มี Unit Tests ด้วย Jest

## 📋 ข้อกำหนดเบื้องต้น

- Node.js (แนะนำเวอร์ชัน 16+)
- npm หรือ Yarn

## 🚀 การติดตั้ง

1. **Clone Repository:**
```bash
git https://github.com/Watthachai/primo_test.git
cd promi_test
```

หรือสร้างโครงสร้างโฟลเดอร์เอง:
```bash
mkdir merge-sorted-arrays
cd merge-sorted-arrays
mkdir src tests
touch src/merge.ts tests/merge.test.ts package.json tsconfig.json jest.config.js
```

2. **ติดตั้ง Dependencies:**
```bash
npm install
# หรือ
yarn install
```

## 🧪 การรัน Unit Tests

```bash
npm test
# หรือ
yarn test
```

## 🔨 การคอมไพล์โค้ด (ทางเลือก)

```bash
npm run build
# หรือ
yarn build
```

## 🧠 คำอธิบาย Logic การทำงาน

### ฟังก์ชัน merge

ฟังก์ชันนี้รวม `collection_1` (เรียงน้อยไปมาก), `collection_2` (เรียงมากไปน้อย), และ `collection_3` (เรียงน้อยไปมาก) เข้าด้วยกัน

#### ขั้นตอนการทำงาน:

1. **การเตรียม collection_2:**
    - กลับลำดับ `collection_2` จากมากไปน้อยให้เป็นน้อยไปมาก
    - เก็บในอาร์เรย์ `col2_ascending`

2. **การรวม (Merge) ด้วย Three Pointers:**
    - สร้างตัวชี้ `ptr1`, `ptr2`, `ptr3` สำหรับแต่ละอาร์เรย์
    - สร้างอาร์เรย์ `result` เปล่า
    - วนลูปทำงานตราบใดที่ยังมีข้อมูลเหลืออยู่ในอาร์เรย์ใดอาร์เรย์หนึ่ง:
      - เปรียบเทียบค่าปัจจุบันจากทั้ง 3 อาร์เรย์
      - เพิ่มค่าที่น้อยที่สุดเข้า `result`
      - เลื่อนตัวชี้ของอาร์เรย์ที่ถูกเลือก
    - คืนค่าอาร์เรย์ผลลัพธ์

#### ประสิทธิภาพ:
- **Time Complexity:** O(N) โดยที่ N คือจำนวนข้อมูลทั้งหมดในอาร์เรย์อินพุตรวมกัน
- **Space Complexity:** O(N) สำหรับอาร์เรย์ผลลัพธ์
