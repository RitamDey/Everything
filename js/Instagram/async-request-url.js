/**
  * JS: async/await
  * New feature in ES7
  * Works in browser
**/


let url = "https://api.github.com";


async function fetchAsync() {
    const response = await fetch(url);
    return await response.json();
}


const response = await fetchAsync();
fetchAsync().then(console.log);
