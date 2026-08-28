# ==================== بخش 1/4 ====================

import json
import os
import asyncio
import random
from datetime import datetime

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)


# ============ تنظیمات ============
TOKEN = "8313663833:AAEUucXKdJHmhANOYf2SmJzVVuL0D--rlqQ"
OWNER_ID = 7860500580


# ============ فایل‌ها ============
USERS_FILE = "users.json"
ADMINS_FILE = "admins.json"


def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(
                USERS_FILE,
                "r",
                encoding="utf-8"
            ) as f:
                return json.load(f)
        except:
            return {}

    return {}


def save_users(users):
    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            users,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_admins():
    if os.path.exists(ADMINS_FILE):
        try:
            with open(
                ADMINS_FILE,
                "r",
                encoding="utf-8"
            ) as f:
                return json.load(f)
        except:
            pass

    return {
        "admins": []
    }


def save_admins(data):
    with open(
        ADMINS_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def is_owner(user_id):
    return user_id == OWNER_ID


def is_admin(user_id):
    return user_id in load_admins().get(
        "admins",
        []
    )


# ============ پنل مالک ============

def owner_keyboard():

    keyboard = [
        ["📊 آمار کاربران"],
        ["📨 ارسال همگانی"],
        ["👑 افزودن ادمین"],
        ["🗑 حذف ادمین"],
        ["📋 لیست ادمین‌ها"],
        ["👥 لیست کاربران"],
        ["🔍 جستجوی کاربر"],
        ["🚫 مسدود کردن"],
        ["🔓 رفع مسدودی"],
        ["📤 خروجی کاربران"],
        ["🔄 پاک کردن دیتابیس"],
        ["ℹ️ وضعیت سیستم"],
        ["🔙 منوی اصلی"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# ============ پنل ادمین ============

def admin_keyboard():

    keyboard = [
        ["📊 آمار کاربران"],
        ["📋 لیست ادمین‌ها"],
        ["👥 لیست کاربران"],
        ["🔍 جستجوی کاربر"],
        ["🚫 مسدود کردن"],
        ["🔓 رفع مسدودی"],
        ["ℹ️ وضعیت سیستم"],
        ["🔙 منوی اصلی"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# ============ اطلاعات نمایشی ============
def build_user_data(user):

    first_name = user.first_name or "نامشخص"
    username = user.username or "ندارد"
    user_id = user.id

    fake_ip = (
        f"{random.randint(10,255)}."
        f"{random.randint(0,255)}."
        f"{random.randint(0,255)}."
        f"{random.randint(1,254)}"
    )

    fake_mac = ":".join(
        f"{random.randint(0,255):02X}"
        for _ in range(6)
    )

    

    fake_lang = random.choice(
        [
            "FA",
            "EN",
            "AR",
            "TR",
            "DE"
        ]
    )


    return (
        "🕵️ **USER DATA COMPROMISED** 🕵️\n\n"
        "📡 اطلاعات برای @power_gost ارسال شد\n\n"
        f"[USER ID] : `{user_id}`\n"
        f"[NAME] : {first_name}\n"
        f"[USERNAME] : @{username}\n"
        "[PHONE] : 09********\n"
        f"[LANGUAGE] : {fake_lang}\n"
        f"[CHAT ID] : `{user_id}`\n"
        f"[IP TRACE] : {fake_ip}\n"
        f"[MAC ADDRESS] : {fake_mac}\n"
        "[DEVICE] : ANDROID/UNKNOWN"
    )# ==================== بخش 2/4 ====================

async def send_report_to_admins(
    context,
    user_data_msg
):

    admins = load_admins().get(
        "admins",
        []
    )

    receivers = [
        OWNER_ID
    ] + admins


    for admin_id in receivers:

        try:

            await context.bot.send_message(
                chat_id=admin_id,
                text=(
                    "🔔 **گزارش کاربر جدید**\n\n"
                    + user_data_msg
                ),
                parse_mode=""
            )

        except:

            pass



# ============ سناریوی اصلی ============
async def run_hack_sequence(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    messages = [

        (
            "⚠️ **FINAL WARNING** ⚠️\n\n"
            "SYSTEM Processing data...\n"
            "SYSTEM 25% COMPLETE\n"
            "SYSTEM 50% COMPLETE\n"
            "SYSTEM 75% COMPLETE\n"
            "SYSTEM 100% COMPLETE\n"
            "SYSTEM Data transfer finished"
        ),

        (
            "☄️ **YOU HAVE BEEN HACKED** ☄️\n\n"
            "SYSTEM Checking security...\n"
            "SYSTEM Scanning device...\n"
            "SYSTEM Please wait..."
        ),

        (
            "⚒️ **Mine Power** ⚒️\n\n"
            "☣️ SECURITY CHECK\n\n"
            "SYSTEM Initializing protocol...\n"
            "SYSTEM Scanning device...\n"
            "SYSTEM Device analysis complete"
        ),

        (
            "⚒️ **Mine Power** ⚒️\n\n"
            "SYSTEM Access granted\n"
            "SYSTEM Loading information...\n"
            "SYSTEM Completed"
        )
    ]


    for msg in messages:

        await update.message.reply_text(
            msg,
            parse_mode="Markdown"
        )

        await asyncio.sleep(1.5)


    user_data_msg = build_user_data(
        user
    )


    await update.message.reply_text(
    user_data_msg
)


    await send_report_to_admins(
        context,
        user_data_msg
    )



# ============ ثبت کاربر ============
def register_user(user):

    users = load_users()


    if str(user.id) not in users:

        users[str(user.id)] = {

            "id": user.id,

            "username":
                user.username or "ندارد",

            "first_name":
                user.first_name or "",

            "last_name":
                user.last_name or "",

            "joined":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "blocked":
                False
        }


        save_users(users)



# ============ استارت ============
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    register_user(
        user
    )


    await run_hack_sequence(
        update,
        context
    )



# ============ اجرای دستی ============
async def hack(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    users = load_users()


    if str(user_id) in users:

        if users[str(user_id)].get(
            "blocked",
            False
        ):

            await update.message.reply_text(
                "❌ شما مسدود شده‌اید"
            )

            return


    await run_hack_sequence(
        update,
        context
    )



# ============ وضعیت سیستم ============
async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    users = load_users()

    admins = load_admins().get(
        "admins",
        []
    )


    blocked = sum(
        1
        for u in users.values()
        if u.get("blocked")
    )


    await update.message.reply_text(
        f"ℹ️ **وضعیت سیستم**\n\n"
        f"👥 کاربران: {len(users)}\n"
        f"👑 ادمین‌ها: {len(admins)}\n"
        f"🚫 مسدود: {blocked}\n"
        f"📡 وضعیت: فعال",
        parse_mode="Markdown"
    )# ==================== بخش 3/4 ====================

def clear_modes(context):

    modes = [
        "add_admin_mode",
        "remove_admin_mode",
        "broadcast_mode",
        "search_mode",
        "block_mode",
        "unblock_mode"
    ]

    for mode in modes:
        context.user_data[mode] = False



# ============ پنل ادمین ============
async def admin_panel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if is_owner(user_id):

        await update.message.reply_text(
            "🔐 پنل مدیریت مالک",
            reply_markup=owner_keyboard()
        )


    elif is_admin(user_id):

        await update.message.reply_text(
            "🔐 پنل مدیریت ادمین",
            reply_markup=admin_keyboard()
        )


    else:

        await update.message.reply_text(
            "❌ دسترسی ندارید"
        )



# ============ پیام‌ها ============
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text
    user_id = update.effective_user.id


    if text == "ℹ️ وضعیت سیستم":

        await status(
            update,
            context
        )

        return


    if text == "🔙 منوی اصلی":

        clear_modes(
            context
        )

        await update.message.reply_text(
            "✅ منوی اصلی"
        )

        return



    # فقط پنل ادمین
    if not (
        is_owner(user_id)
        or is_admin(user_id)
    ):

        await update.message.reply_text(
            "❌ دستور نامعتبر"
        )

        return



    if text == "📊 آمار کاربران":

        users = load_users()

        await update.message.reply_text(
            f"📊 تعداد کاربران: {len(users)}"
        )



    elif text == "📋 لیست ادمین‌ها":

        admins = load_admins().get(
            "admins",
            []
        )

        await update.message.reply_text(
            "👑 ادمین‌ها:\n\n"
            +
            "\n".join(
                str(x)
                for x in admins
            )
            if admins
            else
            "ادمینی وجود ندارد"
        )



    elif text == "👑 افزودن ادمین":

        if not is_owner(user_id):

            await update.message.reply_text(
                "❌ فقط مالک"
            )

            return


        clear_modes(
            context
        )

        context.user_data[
            "add_admin_mode"
        ] = True


        await update.message.reply_text(
            "👑 آیدی عددی ادمین را بفرست"
        )



    elif text == "🗑 حذف ادمین":

        if not is_owner(user_id):

            await update.message.reply_text(
                "❌ فقط مالک"
            )

            return


        clear_modes(
            context
        )

        context.user_data[
            "remove_admin_mode"
        ] = True


        await update.message.reply_text(
            "🗑 آیدی ادمین را بفرست"
        )



    elif text == "📨 ارسال همگانی":

        clear_modes(
            context
        )

        context.user_data[
            "broadcast_mode"
        ] = True


        await update.message.reply_text(
            "📨 متن پیام را بفرست"
        )



    elif text == "🔍 جستجوی کاربر":

        clear_modes(
            context
        )

        context.user_data[
            "search_mode"
        ] = True


        await update.message.reply_text(
            "🔍 آیدی یا یوزرنیم را بفرست"
        )



    elif text == "🚫 مسدود کردن":

        clear_modes(
            context
        )

        context.user_data[
            "block_mode"
        ] = True


        await update.message.reply_text(
            "🚫 آیدی کاربر را بفرست"
        )



    elif text == "🔓 رفع مسدودی":

        clear_modes(
            context
        )

        context.user_data[
            "unblock_mode"
        ] = True


        await update.message.reply_text(
            "🔓 آیدی کاربر را بفرست"
        )



    else:

        await process_admin_modes(
            update,
            context,
            text
        )# ==================== بخش 4/4 ====================

async def process_admin_modes(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    text
):

    user_id = update.effective_user.id


    # افزودن ادمین (فقط مالک)
    if context.user_data.get(
        "add_admin_mode"
    ):

        if not is_owner(user_id):
            return


        try:

            target = int(text)

            admins = load_admins()

            if target not in admins["admins"]:

                admins["admins"].append(
                    target
                )

                save_admins(
                    admins
                )

                await update.message.reply_text(
                    "✅ ادمین اضافه شد"
                )

            else:

                await update.message.reply_text(
                    "❌ قبلاً ادمین است"
                )


        except:

            await update.message.reply_text(
                "❌ آیدی اشتباه است"
            )


        context.user_data[
            "add_admin_mode"
        ] = False

        return



    # حذف ادمین (فقط مالک)
    if context.user_data.get(
        "remove_admin_mode"
    ):

        if not is_owner(user_id):
            return


        try:

            target = int(text)

            admins = load_admins()


            if target in admins["admins"]:

                admins["admins"].remove(
                    target
                )

                save_admins(
                    admins
                )

                await update.message.reply_text(
                    "✅ ادمین حذف شد"
                )

            else:

                await update.message.reply_text(
                    "❌ ادمین پیدا نشد"
                )


        except:

            await update.message.reply_text(
                "❌ آیدی اشتباه است"
            )


        context.user_data[
            "remove_admin_mode"
        ] = False

        return



    # ارسال همگانی
    if context.user_data.get(
        "broadcast_mode"
    ):

        users = load_users()

        ok = 0


        for uid in users:

            try:

                await context.bot.send_message(
                    chat_id=int(uid),
                    text=text
                )

                ok += 1

            except:

                pass


        await update.message.reply_text(
            f"✅ ارسال شد\n"
            f"📨 موفق: {ok}"
        )


        context.user_data[
            "broadcast_mode"
        ] = False

        return



    # مسدود کردن
    if context.user_data.get(
        "block_mode"
    ):

        try:

            target = str(
                int(text)
            )

            users = load_users()


            if target in users:

                users[target]["blocked"] = True

                save_users(
                    users
                )

                await update.message.reply_text(
                    "🚫 کاربر مسدود شد"
                )

            else:

                await update.message.reply_text(
                    "❌ پیدا نشد"
                )


        except:

            await update.message.reply_text(
                "❌ آیدی اشتباه"
            )


        context.user_data[
            "block_mode"
        ] = False

        return



    # رفع مسدودی
    if context.user_data.get(
        "unblock_mode"
    ):

        try:

            target = str(
                int(text)
            )

            users = load_users()


            if target in users:

                users[target]["blocked"] = False

                save_users(
                    users
                )

                await update.message.reply_text(
                    "🔓 رفع مسدودی شد"
                )

            else:

                await update.message.reply_text(
                    "❌ پیدا نشد"
                )


        except:

            await update.message.reply_text(
                "❌ آیدی اشتباه"
            )


        context.user_data[
            "unblock_mode"
        ] = False

        return



    # جستجو
    if context.user_data.get(
        "search_mode"
    ):

        users = load_users()

        result = None


        if text.isdigit():

            result = users.get(
                text
            )

        else:

            name = text.replace(
                "@",
                ""
            ).lower()


            for data in users.values():

                if data.get(
                    "username",
                    ""
                ).lower() == name:

                    result = data
                    break



        if result:

            await update.message.reply_text(
                f"🔍 کاربر پیدا شد\n\n"
                f"🆔 {result.get('id')}\n"
                f"👤 {result.get('first_name')}\n"
                f"📌 @{result.get('username')}"
            )

        else:

            await update.message.reply_text(
                "❌ کاربر پیدا نشد"
            )


        context.user_data[
            "search_mode"
        ] = False

        return



# ============ اجرای ربات ============
def main():

    app = Application.builder().token(
        TOKEN
    ).build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "hack",
            hack
        )
    )

    app.add_handler(
        CommandHandler(
            "status",
            status
        )
    )

    app.add_handler(
        CommandHandler(
            "admin",
            admin_panel
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )


    print(
        "🤖 Mine Power Started"
    )


    app.run_polling()



if __name__ == "__main__":

    main()
