from collections import Counter

from tools.functions import handling_student

weights = {
    'python':{'jun': Counter({'Git': 238,
          'Linux': 334,
          'PostgreSQL': 207,
          'Python': 776,
          'SQL': 430}),
 'mid': Counter({'Bash': 54,
          'C++': 114,
          'Django Framework': 111,
          'Docker': 73,
          'Java': 101,
          'JavaScript': 74,
          'MongoDB': 42,
          'MySQL': 59,
          'Английский язык': 55,
          'ООП': 50}),
 'sin': Counter({'Airflow': 4,
          'AngularJS': 3,
          'MS Access': 3,
          'SOAP': 3,
          'Shell Scripting': 4,
          'Tensorflow': 3,
          'asyncio': 3,
          'highload': 3,
          'kotlin': 4,
          'Алгоритмы и структуры данных': 3,
          'Многопоточность': 3,
          'Нагрузочное тестирование': 4,
          'Сетевые технологии': 3,
          'Системное мышление': 3,
          'Управление разработкой': 3})}

, 'Java': {'jun': Counter({'Android': 139,
          'Git': 247,
          'Java': 596,
          'PostgreSQL': 141,
          'SQL': 244,
          'Spring Framework': 215}),
 'mid': Counter({'Android SDK': 55,
          'Apache Maven': 55,
          'Atlassian Jira': 52,
          'Hibernate ORM': 82,
          'Java SE': 79,
          'JavaScript': 64,
          'Kotlin': 81,
          'Linux': 91,
          'Python': 62,
          'ООП': 68}),
 'sin': Counter({'Cassandra': 3,
          'Intellij IDEA': 5,
          'J2EE': 3,
          'MS Visio': 3,
          'Maven': 4,
          'Microservices': 5,
          'Multithread Programming': 4,
          'Objective-C': 3,
          'Swift': 3,
          'Symfony': 4,
          'TeamCity': 4,
          'gRPC': 4,
          'kubernetes': 3,
          'Аналитическое мышление': 3,
          'Работа с базами данных': 3})}

, 'Javascript': {'jun': Counter({'CSS': 319,
          'CSS3': 155,
          'Git': 431,
          'HTML': 291,
          'HTML5': 225,
          'JavaScript': 765,
          'MySQL': 179,
          'Node.js': 159,
          'PHP': 171,
          'React': 163,
          'SQL': 143,
          'jQuery': 142}),
 'mid': Counter({'AngularJS': 74,
          'C#': 57,
          'Java': 73,
          'Linux': 83,
          'PostgreSQL': 109,
          'Python': 78,
          'Redux': 60,
          'TypeScript': 99,
          'Английский язык': 46,
          'ООП': 98}),
 'sin': Counter({'Apache Maven': 7,
          'Express': 3,
          'JUnit': 4,
          'Kafka': 4,
          'Nuxt': 3,
          'React.JS': 3,
          'SOAP': 3,
          'Software Development': 3,
          'UML': 3,
          'Web Application Development': 4,
          'WebSocket': 4,
          'gRPC': 4,
          'npm': 3,
          'reactjs': 3,
          'Управление разработкой': 4})}

, 'DS': {'jun': Counter({'Git': 27,
          'Linux': 28,
          'Python': 138,
          'SQL': 96,
          'sklearn': 33,
          'Английский язык': 31}),
 'mid': Counter({'Big Data': 12,
          'C++': 11,
          'Data Analysis': 16,
          'Hadoop': 14,
          'MS SQL': 12,
          'Machine Learning': 13,
          'PostgreSQL': 11,
          'Spark': 19,
          'Анализ данных': 12,
          'Математическая статистика': 20}),
 'sin': Counter({'Clickhouse': 2,
          'Databases': 2,
          'Keras': 2,
          'Mathcad': 1,
          'Natural Language Processing': 1,
          'Pytorch': 2,
          'R/Python': 1,
          'airflow': 2,
          'kafka': 2,
          'Анализ рисков': 1,
          'Написание научных статей': 1,
          'Научная деятельность': 1,
          'Научные исследования': 1,
          'Технический английский': 1,
          'Управление рисками': 1})}

, 'Продукт': {'jun': Counter({'B2B Продажи': 176,
          'Активные продажи': 169,
          'Английский язык': 284,
          'Ведение переговоров': 203,
          'Работа в команде': 242,
          'Управление проектами': 215}),
 'mid': Counter({'Agile Project Management': 80,
          'MS PowerPoint': 109,
          'Product Management': 121,
          'Деловая коммуникация': 83,
          'Запуск новых продуктов': 81,
          'Маркетинговый анализ': 116,
          'Проведение презентаций': 94,
          'Продвижение бренда': 76,
          'Развитие продаж': 82,
          'Управление продуктом': 145}),
 'sin': Counter({'Brand Management': 5,
          'Broker': 4,
          'Business Analysis': 8,
          'C++': 6,
          'Investment Banking': 5,
          'Launching new products': 5,
          'MS SQL': 4,
          'MySQL': 5,
          'Startup': 5,
          'growth hacking': 5,
          'user growth': 5,
          'Биржевые торги': 4,
          'Взаимодействие с инвестиционными фондами': 4,
          'Лидерство': 4,
          'Финансовая отчетность': 5})}

, 'Прожект': {'jun': Counter({'Agile Project Management': 112,
          'Atlassian Jira': 80,
          'MS PowerPoint': 100,
          'MS Project': 112,
          'Project management': 93,
          'Scrum': 79,
          'Английский язык': 185,
          'Бизнес-анализ': 68,
          'Ведение переговоров': 113,
          'Грамотная речь': 85,
          'Деловая коммуникация': 119,
          'Деловая переписка': 67,
          'Деловое общение': 61,
          'Организаторские навыки': 106,
          'Проектный менеджмент': 56,
          'Работа в команде': 227,
          'Разработка технических заданий': 59,
          'Управление командой': 72,
          'Управление продуктом': 60,
          'Управление проектами': 455}),
 'mid': Counter({'CRM': 34,
          'MS Visio': 34,
          'PMBOK': 39,
          'Product Management': 31,
          'Аналитическое мышление': 34,
          'Креативность': 34,
          'Ориентация на результат': 40,
          'Проведение презентаций': 29,
          'Проектная документация': 30,
          'Управление рисками': 62}),
 'sin': Counter({'Business Analysis': 7,
          'Business English': 6,
          'Google AdWords': 4,
          'Launching new products': 5,
          'Sales Skills': 5,
          'Start-up project': 5,
          'Startup': 5,
          'Teamleading': 6,
          'growth hacking': 5,
          'user growth': 5,
          'Аналитика продаж': 5,
          'Вывод продукта на рынок': 5,
          'Маркетинговые коммуникации': 4,
          'Участие в Тендерах': 4,
          'Финансовая отчетность': 7})}
}


if __name__ == '__main__':
    handling_student(weights)
