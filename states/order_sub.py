from aiogram.fsm.state import StatesGroup, State


class OrderSubscription(StatesGroup):
    choosing_subscription = State()

