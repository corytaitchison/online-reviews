# SCDL1991 Sem 2 - 10. Supporting Consumer Decision Using Online Reviews

## Getting Started

### Install the Git Repository

**Option 1 - Use the GitHub client**

1. Download GitHub for your computer [here](https://desktop.github.com/).
2. Choose `Clone Repository`, and enter the URL: https://github.com/corytaitchison/online-reviews.git

**Option 2 - Use the Command Line** (Not recommended)

1. Open Terminal and navigate to your documents folder / where you want to download the files
2. Run

```bash
git clone https://github.com/corytaitchison/online-reviews.git && cd online-reviews
```

### Install the python requirements

1. Open terminal
2. Check that you have python installed
   (should be `3.7.x`)

```bash
python --version
## Or
python3 --version
```

3. Install the necessary packages

```bash
pip install -r requirements.txt
```

### Download the data (if you haven't already)

**Option 1: Download the pre-formatted CSV**

_Coming soon_

**Option 2: Download the JSON file**

- [Yelp Dataset](https://www.yelp.com/dataset/download)

---

## GitHub Tips

GitHub is a tool to assist collaboration on projects, with a main feautre being that it tracks changes and intelligently merges any conflicts when two people edit the same document.

Some terminology to know:

- Whenever you want to work on a project, you should first **PULL** or **FETCH** from the repository, to download the latest changes.
- Once you edit a file, you need to **COMMIT** it to "save" the changes. Add a brief summary message to tell us what you changed.
- When you're done editing, you **PUSH** all your commits back to the repository, so that other people can download your changes. If you commit but do not push, then other people can't see your changes.

In the GitHub application, it tells you all the files you've edited, and you can choose which ones to comit. You can also view the history, and see who edited what and when.

Sometimes, Git can't merge two changes because people edited the same part of the code. It will tell you there's a merge conflict, and you may need to go through and choose which parts to keep / discard.

If you want to learn more, check out these [labs](https://lab.github.com/githubtraining/introduction-to-github).
