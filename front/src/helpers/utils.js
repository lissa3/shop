export const range = (start, end) => {
    // [1, 2, 3, 4]
   return [...Array(end).keys()].map(el => el + start)
}