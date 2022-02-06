# Shineka Verification Bot Property Of TheShineka
# ShinekaVerification © @DIPUID © TheShineka
# Owner DIPUID and TheShineka






async def MakeCaptchaMarkup(markup, __emoji, indicator):
    __markup = markup
    for i in markup:
        for k in i:
            if k["text"] == __emoji:
                k["text"] = f"{indicator}"
                k["callback_data"] = "HeHe"
                return __markup
