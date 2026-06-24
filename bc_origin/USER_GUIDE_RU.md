# BC-Origin Shadow Lab — руководство пользователя

**GitHub:** https://github.com/AIDevelopersMonster/boundary-compensation  
**Рабочая ветка:** `codex/bc-origin`  
**Draft PR:** https://github.com/AIDevelopersMonster/boundary-compensation/pull/5

Это руководство объясняет, как устроены файлы BC-Origin на GitHub, как запускать программы, где искать результаты и что делать при типичных ошибках Windows/Python.

---

## 1. Где находятся материалы

Вся текущая работа по BC-Origin лежит в ветке:

```text
codex/bc-origin
```

До merge в `main` обычный просмотр основной ветки может не показывать новые файлы. Чтобы увидеть их на GitHub:

1. открыть PR #5: https://github.com/AIDevelopersMonster/boundary-compensation/pull/5;
2. перейти во вкладку **Files changed**;
3. или локально переключиться на ветку `codex/bc-origin`.

Локально:

```bash
git fetch origin
git switch codex/bc-origin
git pull
```

---

## 2. Структура папок

Основная папка программы:

```text
bc_origin/
```

Внутри:

```text
bc_origin/
  README.md                         # краткое описание BC-Origin
  USER_GUIDE_RU.md                  # это руководство
  article/
    BC-Origin-I-v0.1.0-draft.md     # рабочий текст статьи
  docs/
    00_program_definition.md        # определение программы
    01_article_skeleton.md          # скелет статьи
    02_experiment_protocol.md       # протокол экспериментов
    03_core_effects.md              # три основных эффекта
    04_structural_coupling_and_multishadow_branch.md
                                      # ветка BC-Origin II
  lab/
    README.md                       # техническое описание лаборатории
    requirements.txt                # Python-зависимости
    run_windows.ps1                 # запуск через PowerShell
    run_windows.bat                 # запуск без PowerShell-политик
    web/
      index.html                    # standalone GUI в браузере
    python/
      bc_origin_visual_core.py      # вычислительное ядро
      generate_visuals.py           # генератор PNG-графиков
    outputs/                        # сюда создаются картинки
    streamlit_app.py                # опциональный Streamlit GUI
  prompts/
    01_strong_theory_builder.md
    02_adversarial_reviewer.md
    03_formal_math_reviewer.md
    04_computational_experimenter.md
    05_publication_auditor.md
```

---

## 3. Самый простой запуск: один клик

В корне репозитория есть файл:

```text
START_BC_ORIGIN_WINDOWS.bat
```

Запуск:

```cmd
START_BC_ORIGIN_WINDOWS.bat
```

или двойной клик по файлу в Проводнике Windows.

Он делает следующее:

1. создаёт локальное виртуальное окружение `.venv-bc-origin`;
2. устанавливает зависимости из `bc_origin/lab/requirements.txt`;
3. запускает генератор графиков;
4. открывает папку с результатами;
5. открывает браузерный GUI.

Этот способ не требует вручную менять PowerShell Execution Policy.

---

## 4. Запуск GUI без Python

Интерактивный браузерный GUI не требует Python, pip или установки зависимостей.

Файл:

```text
bc_origin/lab/web/index.html
```

Запуск из корня репозитория:

```powershell
start .\bc_origin\lab\web\index.html
```

Или открыть файл двойным кликом.

В GUI можно двигать параметры:

```text
n1, n2, gamma, kappa, d1, d2, mu
```

GUI показывает:

- orientation product `s = sign(n1*n2)`;
- матрицу `D_signed`;
- eigen-denominators `lambda-`, `lambda+`;
- scale ratios `ell/L`;
- состояние admissibility / horizon crossed.

---

## 5. Генерация статических графиков через Python

Требуется установленный Python 3 и пакеты:

```text
numpy
matplotlib
```

Установка зависимостей:

```powershell
python -m pip install -r bc_origin\lab\requirements.txt
```

Запуск генератора:

```powershell
python bc_origin\lab\python\generate_visuals.py --out bc_origin\lab\outputs
```

После успешного запуска появятся файлы:

```text
bc_origin/lab/outputs/spectrum_signed_shift.png
bc_origin/lab/outputs/admissibility_horizon.png
bc_origin/lab/outputs/phase_map.png
bc_origin/lab/outputs/model_scheme.png
```

Смысл файлов:

```text
spectrum_signed_shift.png
  Показывает, как sign channel сдвигает ветви lambda+ и lambda-.

admissibility_horizon.png
  Показывает критическую кривую gamma_c(kappa), где lambda- = 0.

phase_map.png
  Карта областей: локализованная тень / horizon-crossed branch.

model_scheme.png
  Схема: hidden winding -> scale channel + sign channel -> observable shadow.
```

---

## 6. Запуск через BAT без PowerShell-политик

Если PowerShell блокирует `.ps1`-скрипты, используйте:

```cmd
bc_origin\lab\run_windows.bat
```

Он устанавливает зависимости и запускает генератор без изменения PowerShell Execution Policy.

---

## 7. Запуск через PowerShell

Файл:

```text
bc_origin/lab/run_windows.ps1
```

Если PowerShell разрешает запуск scripts:

```powershell
.\bc_origin\lab\run_windows.ps1
```

Если появляется ошибка:

```text
execution of scripts is disabled on this system
```

можно запустить временно с обходом политики:

```powershell
powershell -ExecutionPolicy Bypass -File .\bc_origin\lab\run_windows.ps1
```

Или разрешить scripts для текущего пользователя:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## 8. Опциональный Streamlit GUI

Streamlit-версия находится здесь:

```text
bc_origin/lab/streamlit_app.py
```

Установка:

```powershell
python -m pip install streamlit numpy matplotlib
```

Запуск:

```powershell
streamlit run bc_origin\lab\streamlit_app.py
```

Streamlit удобен для демонстрации параметров, фазовой карты и текущих значений спектра в более привычном веб-интерфейсе.

---

## 9. Как устроена математика программы

Основная скрытая структура:

```text
h = (q, n)
```

где:

```text
q = index-like residual type
n = oriented winding number
```

Winding number даёт два канала:

```text
scale channel = |n|
sign channel  = sign(n)
```

Одногенераторная шкала:

```text
ell/L = mu_|q| / (2*pi*|n| - theta(|q|))
```

Двухтеневой signed operator:

```text
s = sign(n1*n2)

D_signed = [[d1 + gamma*s, kappa],
            [kappa,        d2 + gamma*s]]
```

Eigen-denominators:

```text
lambda_pm = (d1+d2)/2 + gamma*s +/- sqrt(((d1-d2)/2)^2 + kappa^2)
```

Локализованная тень допустима только если:

```text
lambda_pm > 0
```

Если:

```text
lambda_pm = 0
```

то:

```text
ell/L -> infinity
```

Это называется admissibility horizon.

---

## 10. Три основных эффекта BC-Origin I

### 1. Orientation-controlled shadow localization

Если `s = +1`, inverse-scale denominator растёт, а наблюдаемая тень сжимается.

Если `s = -1`, denominator падает, а наблюдаемая тень размывается.

### 2. Admissibility horizon

Когда ветвь достигает `lambda = 0`, локализованная наблюдаемая тень исчезает как допустимый объект модели.

### 3. Coupling-induced shadow gap

Off-diagonal coupling `kappa` разделяет две ветви:

```text
lambda_plus - lambda_minus = 2*sqrt(((d1-d2)/2)^2 + kappa^2)
```

---

## 11. Типичные проблемы Windows

### Проблема: `python --version` пишет только `Python`

Это Windows Store alias, а не настоящий Python.

Проверка:

```powershell
where.exe python
```

Если видно:

```text
C:\Users\...\AppData\Local\Microsoft\WindowsApps\python.exe
```

нужно отключить alias:

```text
Settings -> Apps -> Advanced app settings -> App execution aliases
```

Отключить:

```text
python.exe
python3.exe
```

После этого поставить Python с https://www.python.org/downloads/windows/ и включить `Add python.exe to PATH`.

### Проблема: `ModuleNotFoundError: No module named 'matplotlib'`

Установить зависимости:

```powershell
python -m pip install -r bc_origin\lab\requirements.txt
```

или:

```powershell
python -m pip install numpy matplotlib
```

### Проблема: PowerShell блокирует `.ps1`

Использовать `.bat`:

```cmd
bc_origin\lab\run_windows.bat
```

или:

```powershell
powershell -ExecutionPolicy Bypass -File .\bc_origin\lab\run_windows.ps1
```

---

## 12. Как обновлять проект с GitHub

Если ветка уже есть локально:

```bash
git switch codex/bc-origin
git pull
```

Если ветки ещё нет:

```bash
git fetch origin
git switch codex/bc-origin
```

После merge PR #5 в `main` можно будет работать из `main`:

```bash
git switch main
git pull
```

---

## 13. Что публиковать на Zenodo

Для Zenodo текущий набор файлов:

```text
BC-Origin-I-v0.1.0-preprint.pdf
BC-Origin-I-v0.1.0-Zenodo-LaTeX-package.zip
BC-Origin-I-v0.1.0-review-pack.pdf
```

Рекомендация:

1. основной файл: `BC-Origin-I-v0.1.0-preprint.pdf`;
2. source package: `BC-Origin-I-v0.1.0-Zenodo-LaTeX-package.zip`;
3. review pack — supplementary file или внутренний аудит.

В описание Zenodo добавить ссылку на GitHub:

```text
https://github.com/AIDevelopersMonster/boundary-compensation
```

До merge можно добавить ссылку на PR:

```text
https://github.com/AIDevelopersMonster/boundary-compensation/pull/5
```

---

## 14. Что делать дальше

BC-Origin I уже содержит:

```text
oriented winding -> scale/sign channels -> two-shadow localization/horizon/gap
```

Следующая исследовательская ветка:

```text
BC-Origin II: Structural Coupling and Multi-Shadow Geometry
```

Главная задача BC-Origin II:

```text
kappa should become a structural overlap value, not a fitted constant
```

Кандидат:

```text
kappa_ij = <u_ni, A u_nj> = 1/(1 + (n_i-n_j)^2)
```

Это переводит модель от ручных параметров к структурным операторам.
