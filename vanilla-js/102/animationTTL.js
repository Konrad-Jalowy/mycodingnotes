function animation(strings, ...values) {
    const css = strings.reduce((acc, str, idx) => acc + str + (values[idx] || ''), '');
    return `<style>@keyframes myAnimation { ${css} }</style>`;
}

const anim = animation`
    0% { transform: translateX(0); }
    50% { transform: translateX(100px); }
    100% { transform: translateX(0); }
`;

console.log(anim);
// Output: <style>@keyframes myAnimation { 0% { transform: translateX(0); } 50% { transform: translateX(100px); } 100% { transform: translateX(0); } }</style>
