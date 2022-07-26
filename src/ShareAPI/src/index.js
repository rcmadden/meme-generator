// import "./styles.css";

const shareButton = document.getElementById("shareButton"); 
// does this return the same as document.querySelector?
const urlToFile = async (url) => {
  const response = await fetch(url);
  console.log(response)
  console.log(typeof(response))
  const blob = await response.blob();
  const file = new File([blob], "image.jpg", { type: blob.type });
  return file;
};

shareButton.addEventListener("click", async () => {
  if (window.navigator.share) {
    const file = await urlToFile(
      "https://images.unsplash.com/photo-1575535468632-345892291673?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80"
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
