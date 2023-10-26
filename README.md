flowchart TD
    A[Request] --> B(CreateTrainingView)
    B -- Заходим во View --> C(CreateTrainingHandler)
    C -- Создаем объект тренировки --> D(CreateTrainingService)
    D --> C
    C -- Пуляем сигнал создания VApp ---> E(make_vapp)
    E -- Идем в хэндлер создания VApp --> F(CreateTrainingVAppHandler)
    F -- Ищем горячий или создаем новый VApp --> G(GetTrainingVAppService)
    G --> F
    F -- Пуляем сигнал, идем инициализировать VApp ---> H(init_vapp)
    H -- Запускаем таску создания VApp--> I(create_virtual_application)
    I -- Идем в хендлер создания VApp --> K(CreateVAppHandler)
    K --> L(ChangeVAppSatusService)
    L --> K
    K -- Идем в сервис инициализации VApp --> M(InitVAppService)
    M --> K
    K -- Пуляем сигнал vapp_updated --> vapp_updated
