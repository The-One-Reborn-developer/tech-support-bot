from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)


def medical_organization_keyboard() -> InlineKeyboardMarkup:
    with open('medical_organizations.txt', 'r') as f:
        medical_organizations = f.read().split('\n')
    
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=organization,
                    callback_data=str(organization)
                )
            ]
            for organization in medical_organizations
        ]
        + [[
            InlineKeyboardButton(
                text='Назад в главное меню ◀️',
                callback_data='main'
            )
        ]]
    )