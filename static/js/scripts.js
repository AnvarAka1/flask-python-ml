// let globalIndex = 0;
document.addEventListener("DOMContentLoaded", function() {
	const explanations = document.querySelector("#explanation");
	let numberOfTutorialWindows = 0;
	const makeExplanationsInvisible = exps => {
		for (child of exps.children) {
			child.style.display = "none";
		}
	};
	const makeExplanationVisible = (explanation, exps) => {
		makeExplanationsInvisible(exps);
		exps.children[explanation].style.display = "block";
	};
	if (explanations) makeExplanationsInvisible(explanations);
	const processing = document.querySelectorAll(".processing");
	if (processing.length > 0) {
		processing.forEach((p, index) => {
			p.addEventListener("click", () => {
				if (explanations) {
					makeExplanationVisible(index, explanations);
				}
				fetch(`http://localhost:5000/${p.dataset.url}?_=` + new Date().getTime(), {
					method: "POST", // or 'PUT'
					headers: {
						"Content-Type": "application/json"
					},
					body: `{ "mt": "${p.dataset.id}" }`
				})
					.then(res => {
						return res.json();
					})
					.then(res => {
						const image = `<img src='${res + "?" + new Date().getTime()}' alt='filtered image' />`;
						const imageDiv = document.querySelector("#image");
						const h4 = document.querySelector("#classification");
						const text = `I will tell you with <span id="accuracy">${res.accuracy}%</span> accuracy, that this is a <span id="label">${res.label}</span>`;
						if (h4) {
							h4.innerHTML = text;
						}
						if (imageDiv) {
							imageDiv.innerHTML = image;
						}
					})
					.catch(err => {
						console.log(err);
					});
			});
		});
	}
});
