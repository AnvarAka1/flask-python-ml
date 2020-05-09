let globalIndex = 0;
let tutorialItems = [];
let result = null;
document.addEventListener("DOMContentLoaded", function() {
	const button = document.querySelector("#next");
	const resultId = document.querySelector("#result");
	const title = document.querySelector("#title");
	const exp = document.querySelector("#expl");
	const code = document.querySelector("#code");
	const setTutorialItems = () => {
		title.innerHTML = tutorialItems[globalIndex].title;
		exp.innerHTML = tutorialItems[globalIndex].explanation;
		code.innerHTML = tutorialItems[globalIndex].code;
		if (globalIndex == tutorialItems.length - 1)
			resultId.innerHTML = `
        <p class="text-danger"><strong>Result: ${result.label}</strong></p>
        <p class="text-primary"><strong>Accuracy: ${result.accuracy}%</strong></p>
        `;
	};
	button.addEventListener("click", () => {
		globalIndex++;
		globalIndex %= tutorialItems.length;
		setTutorialItems();
	});
	fetch(`http://localhost:5000/tutorial?_=` + new Date().getTime(), {
		method: "POST", // or 'PUT'
		headers: {
			"Content-Type": "application/json"
			// "Cache-Control": "no-cache, must-revalidate"
		},
		body: `{ "mt": "test" }`
	})
		.then(res => {
			return res.json();
		})
		.then(res => {
			if (title && exp && code) {
				tutorialItems = res.items;
				result = res.result;

				setTutorialItems();
			}
		})
		.catch(err => {
			console.log(err);
		});
});
