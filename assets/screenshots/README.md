//
//  OnboardingContent.swift
//  ZeroBalance
//
//  Created by Hakob Ghlijyan on 29.09.2026.
//  Copyright © 2026. All rights reserved.
//

import Foundation

// MARK: - Onboarding Content Documentation

/// # Onboarding Content Structure / Структура контента Онбординга
///
/// **EN:**
/// This file defines localized strings for the 6-page onboarding flow.
/// It guides users from the basic smart cleaner functionality to Pro features and export capabilities.
///
/// **RU:**
/// Этот файл содержит локализованные строки для 6-страничного экрана онбординга.
/// Он проводит пользователя от базового функционала смарт-клинера до Pro-возможностей и экспорта транзакций.
///
/// - Page 1: Welcome & Smart Cleaner / Приветствие и выбор суммы списания
/// - Page 2: Smart Balance Split / Распределение баланса и умный расчет
/// - Page 3: Transaction History / История всех списаний и операций
/// - Page 4: How It Works & Support / Ознакомительный экран и поддержка разработки
/// - Page 5: Free vs Pro Overview / Возможности бесплатной версии и ограничений
/// - Page 6: Pro Features & Export / Премиум-функции, экспорт в PDF и поддержка автора
///
enum OnboardingContent {
    
    // MARK: - Page 1: Welcome & Smart Cleaner
    
    /// **EN:** Page 1 Title - Welcome and Smart Cleaner launch
    /// **RU:** Страница 1 Заголовок - Приветствие и смарт-клинер
    static let page1Title = String(
        localized: "onboarding.page1.title",
        defaultValue: "Smart Balance Cleaner"
    )
    
    /// **EN:** Page 1 Description - Choose custom amount to clear leftover App Store credit
    /// **RU:** Страница 1 Описание - Выбор точной суммы для списания остатка App Store
    static let page1Desc = String(
        localized: "onboarding.page1.desc",
        defaultValue: "Easily select or enter the exact custom amount you want to zero out in your Apple account balance."
    )
    
    // MARK: - Page 2: Smart Balance Calculation
    
    /// **EN:** Page 2 Title - Calculation and split breakdown
    /// **RU:** Страница 2 Заголовок - Расчет и разбивка списания
    static let page2Title = String(
        localized: "onboarding.page2.title",
        defaultValue: "Calculate & Split"
    )
    
    /// **EN:** Page 2 Description - Detailed split preview between store credit and payment
    /// **RU:** Страница 2 Описание - Наглядное распределение списания на отдельные части
    static let page2Desc = String(
        localized: "onboarding.page2.desc",
        defaultValue: "See the precise breakdown of your remaining balance and calculated parts before confirming the operation."
    )
    
    // MARK: - Page 3: History & Overview
    
    /// **EN:** Page 3 Title - Transaction and activity history
    /// **RU:** Страница 3 Заголовок - История операций и транзакций
    static let page3Title = String(
        localized: "onboarding.page3.title",
        defaultValue: "Track Every Cleared Balance"
    )
    
    /// **EN:** Page 3 Description - Keep records of all previous balance clears
    /// **RU:** Страница 3 Описание - Хранение истории всех прошлых списаний в одном месте
    static let page3Desc = String(
        localized: "onboarding.page3.desc",
        defaultValue: "Access your complete history of cleared balances and keep full control over past transactions."
    )
    
    // MARK: - Page 4: Guidelines & Developer Support
    
    /// **EN:** Page 4 Title - Information, terms, and developer tips
    /// **RU:** Страница 4 Заголовок - Информация, условия и поддержка проекта
    static let page4Title = String(
        localized: "onboarding.page4.title",
        defaultValue: "How It Works & Support"
    )
    
    /// **EN:** Page 4 Description - Explain conditions and small donation support
    /// **RU:** Страница 4 Описание - Ознакомительная часть по условиям и поддержка разработки
    static let page4Desc = String(
        localized: "onboarding.page4.desc",
        defaultValue: "Review fulfilled conditions and how clears work, while supporting indie app development with small tips."
    )
    
    // MARK: - Page 5: Free Features & Settings
    
    /// **EN:** Page 5 Title - Standard features for free tier users
    /// **RU:** Страница 5 Заголовок - Базовые возможности бесплатной версии
    static let page5Title = String(
        localized: "onboarding.page5.title",
        defaultValue: "Free Tier Features"
    )
    
    /// **EN:** Page 5 Description - What free users get out of the box
    /// **RU:** Страница 5 Описание - Описание основных стандартных опций для обычных пользователей
    static let page5Desc = String(
        localized: "onboarding.page5.desc",
        defaultValue: "Standard calculations, basic history view, and essential balance management tools are free for everyone."
    )
    
    // MARK: - Page 6: Pro Upgrade & PDF Export
    
    /// **EN:** Page 6 Title - Pro features, PDF export, and supporting authors
    /// **RU:** Страница 6 Заголовок - Премиум-версия, экспорт в PDF и поддержка
    static let page6Title = String(
        localized: "onboarding.page6.title",
        defaultValue: "Unlock Pro & Export"
    )
    
    /// **EN:** Page 6 Description - Export transactions to PDF, unlock full history, and support creators
    /// **RU:** Страница 6 Описание - Экспорт истории в PDF, дополнительные настройки и поддержка авторов
    static let page6Desc = String(
        localized: "onboarding.page6.desc",
        defaultValue: "Export your transaction history to PDF, customize advanced settings, and support future updates with Pro."
    )
}
