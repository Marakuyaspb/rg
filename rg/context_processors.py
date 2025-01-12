def page_title(request):
    # Get the current path
    path = request.path

    # Logic to determine the title based on the URL
    if path == '/index/':
        title = "Wonderful Cars"

    elif path == '/about/':
        title = "R.E.D. Group Auto - о компании"
    elif path == '/contact/':
        title = "Контакты R.E.D. Group Auto"
    elif path == '/guarantee/':
        title = "Техническая поддержка иномарки - как гарантийное обслуживание"
    elif path == '/insurance/':
        title = "КАСКО по справедливой цене"
    elif path == '/jurists/':
        title = "Юридическое сопровождение покупки иномарки, трейд-ин"
    elif path == '/privacy/':
        title = "Пользовательское соглашение"
    elif path == '/service/':
        title = "ТО, сервисное обслуживание, диагностика"
    elif path == '/spares/':
        title = "Запчасти для иномарок в наличии и под заказ"
    elif path == '/catalog/':
        title = "Купить машину по лучшей цене"
    elif path == '/catalog/fresh/':
        title = "Купить новую машину"
    elif path == '/catalog/used/':
        title = "Купить машину с пробегом"
        
    else:
        title = "R.E.D. Group Auto. Купить иномарку без переплат"

    return {'page_title': title}