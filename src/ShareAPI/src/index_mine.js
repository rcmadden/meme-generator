// import "./styles.css";

const shareButton = document.getElementById("shareButton"); 
// does this return the same as document.querySelector?
const urlToFile = async (url) => {
  const response = await fetch(url);
  console.log(response)
  console.log(typeof(response))
  const blob = await response.blob();
  const file = new File([blob], "{{ path }}", { type: blob.type });
  return file;
};

shareButton.addEventListener("click", async () => {
  if (window.navigator.share) {
    const file = await urlToFile(
      "{{ path }}"
    );
    const files = [file];

    if (!navigator.canShare || !navigator.canShare({ files: files })) {
      alert("Unsupported share feature");
      return;
    }

    navigator
      .share({
        files: files,
        title: "Sweet Shiba Inu"
      })
      .then(() => console.log("Share was successful."))
      .catch((error) => console.log("Sharing failed", error));
  } else {
    alert(`Your browser or operating system doesn't support sharing files.`);
  }
});
