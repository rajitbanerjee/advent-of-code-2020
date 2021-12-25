export const sortString = (e: string) => e.split("").sort().join("");
export const isLowerCase = (s: string) => s === s.toLowerCase();
export const isUpperCase = (s: string) => s === s.toUpperCase();
export const isAlpha = (ch: string) => /^[A-Z]$/i.test(ch);
