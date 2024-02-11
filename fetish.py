from tkinter import Tk, filedialog
from github import Github
import os


def clone_git_repository(repo_url, destination_dir):
    os.system(f'git clone {repo_url} {destination_dir}')


if __name__ == "__main__":
    # Указываем персональный API ключ GitHub
    github_token = input("Введите ваш персональный API ключ GitHub: ")
    # Инициализируем объект GitHub
    g = Github(github_token)

    # Получаем аккаунт пользователя GitHub
    user = g.get_user()

    # Получаем список репозиториев пользователя
    repositories = user.get_repos()

    # Создаем окно Tkinter
    root = Tk()
    root.withdraw()  # скрываем основное окно

    # Показываем диалоговое окно выбора папки
    target_directory = filedialog.askdirectory(
        title="Выберите папку для клонирования репозиториев")

    # Перебираем все репозитории пользователя
    for repo in repositories:
        repository_name = repo.name
        destination_dir = os.path.join(target_directory, repository_name)

        # Проверяем наличие папки с названием репозитория
        if os.path.isdir(destination_dir):
            print(f"Репозиторий {
                  repository_name} уже существует в указанной директории.")
        else:
            # Клонируем репозиторий Git
            clone_git_repository(repo.clone_url, destination_dir)
            print(f"Репозиторий {repository_name} был успешно клонирован.")
