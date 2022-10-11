/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./**/templates/**/*.html"],
    theme: {
        extend: {
            colors: {
                "orange-red": '#FF5E5B',
                "gainsboro": '#D8D8D8',
                "ivory": '#FFFFEA',
                "robin-egg-blue": '#00CECB',
                "corn": '#FFED66',
                "quick-silver": '#A7A2A2',
                "green-apple": "#80DE99",
                "gunmetal": "#1E313BAC",
            },
        }
    },
    plugins: [],
}
