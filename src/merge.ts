/**
 * 
 * @param collection_1 
 * @param collection_2 
 * @param collection_3
 *  จากโจทย์ที่ให้มา
 *  For implementing function with this interface
    merge (int[] collection_1, int[] collection_2, int[] collection_3) : int []
    That returns sorted array by ascending.

    given
        collection_1, collection_3 already sorted from min(0) to max
        collection_2 already sorted from max to min(0)
 */

export function merge (
    collection_1: number[],
    collection_2: number[],
    collection_3: number[],
): number[] {
    const result: number[] = [];


    // 1. ขั้นตอนนี้จะทำการแปลง collection_2 ให้เป็น ascending โดยไม่ใช่การใช้ฟังก์ชัน sort()
    // จากนั้นจะทำการคัดลอกเพื่อหลีกเลี่ยงการแก้ไข array ที่ส่งเข้ามา
    const col2_ascanding: number[] = [];
    for (let i = collection_2.length - 1; i >= 0; i--) {
        col2_ascanding.push(collection_2[i]);
    }

    // 2. ขั้นตอนนี้จะทำการ merge collection_1, collection_2, collection_3
    let ptr1 = 0;
    let ptr2 = 0;
    let ptr3 = 0;

    const len1 = collection_1.length;
    const len2 = col2_ascanding.length;
    const len3 = collection_3.length;

    // loop
    while (ptr1 < len1 || ptr2 < len2 || ptr3 < len3) {
        // รรับค่า และใช้ infinity ถ้าตัว pointer เกินหรือ out of bounds
        const val1 = ptr1 < len1 ? collection_1[ptr1] : Infinity;
        const val2 = ptr2 < len2 ? col2_ascanding[ptr2] : Infinity;
        const val3 = ptr3 < len3 ? collection_3[ptr3] : Infinity;

        // 3. คัดเลือกค่าที่น้อยที่สุด
        if ( val1 <= val2 && val1 <= val3) {
            result.push(val1);
            ptr1++;
        } else if (val2 <= val1 && val2 <= val3) {
            result.push(val2);
            ptr2++;
        }
        else { //ถ้าข้างบนเยอะหมดเลย
            result.push(val3);
            ptr3++;
        }
    }

    return result;
}