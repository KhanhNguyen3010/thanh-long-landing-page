import json

data = [
    {
        "id": "canada",
        "title": "Canada",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCyss7vFf0C-zgsEj6HPHhR-dCSRNcJnJZ1VygxEMwzW0MliirHK4BGzGK4RJE45lXXT3Lwxhiv_tXo1E7WI5EdOlNHmnd2E7t56y6GTc5UfwomHXjqdk0hYgwIAjlaGIVCg9F6geTECYC_od_YedokeFBf7CRSAQc_5qSOoRAhux177BJQkVaR92BmaWXcOWymLH2YTPmhVg1fWKK0KEIMNOLl2eWpdNTDnNSM3V8n8P-FVXIAK92kLHlnHdfaFib8DYM",
        "desc": "Định cư và làm việc lâu dài với nhiều ngành nghề đa dạng, thu nhập hấp dẫn, môi trường sống chất lượng cao hàng đầu thế giới.",
        "tags": ["Lương cao, phúc lợi tốt", "Cơ hội mang theo gia đình", "Lộ trình thẻ xanh rõ ràng"],
        "modal": "canadaModal",
        "btnText": "Chi Tiết",
        "isHot": True,
        "icon": "map"
    },
    {
        "id": "ireland",
        "title": "Ireland",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDIdsTmtuUvX-ohiIZXwicTpB-fjCI4JQJj51sR3TAU9P0dIkQsok2XUZYnmva7dpAwFDiGye9N197U9SU6zKSc7IQOlRina85QRJLXx_g1YQto4j5oQkeA5ktiuB3VO2Zo9BP5yxdIpLI2Y1NB1f7daD5MpwcWF7pncXX6YnhS3d1Y6xqIEN6MG1q0VAyrzrVEOXLgpH5B6_UGT7SmG0iyFWMVzWH9YJSQu6UPtkGJ6JGsAyTACESon6chN6Ia_csoNDg",
        "desc": "Cơ hội làm việc hợp pháp tại Ireland với ngành nông nghiệp (hái nấm). Môi trường làm việc an toàn, thu nhập ổn định và cơ hội định cư lâu dài cho cả gia đình.",
        "tags": ["Thu nhập ổn định ~14 EUR/giờ", "Không yêu cầu tiếng Anh cao", "Cơ hội bảo lãnh gia đình"],
        "modal": "irelandModal",
        "btnText": "Chi Tiết",
        "isHot": False,
        "icon": "agriculture"
    },
    {
        "id": "usa_eb3",
        "title": "USA (EB-3)",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAQlcQIYVrOBRXotY-5cTExeqfF5NoWgDjA2tvz2D0ozLOKxcgpPx8r6SBtfV6DX_6F6iNiAPFAkk1fuOjjiWDchAI6QQhIuWxG2u55GW_7j-RhmIAhS27w6kbeAue37nIg730NG8kalKrXIGW8MYx8D6RR6yqytX_v4HFATTvfw_SroSDM8OSZnDiz98YB2xQ7RtLpu_MWL4MDKANKedw73HZ6ikMMi-VEIYGvP5YQ1WwysoJn5wvkVzLaUD3-S_D2G38",
        "desc": "Chương trình định cư Mỹ chính thức diện lao động phổ thông (EB-3). Lấy Thẻ xanh vĩnh viễn cho cả gia đình với công việc đa dạng, không yêu cầu kinh nghiệm hay bằng cấp cao.",
        "tags": ["Lấy thẻ xanh vĩnh viễn", "Con học trường công miễn phí", "Công việc đa dạng"],
        "modal": "usaModal",
        "btnText": "Chi Tiết",
        "isHot": False,
        "icon": "flag"
    },
    {
        "id": "litva",
        "title": "Litva",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuC4IaqZYqSuKfxCYsJGtaIzV4Dp1gTj9mTlE_qN-4Yk1ih85u4foWuSh0JfBAGysQ5BP76okrhkjaCcZv2gj_bfEpfUKsNVMx4Mr9BK7pbrKFOXU2kxRluGlKM4kAiJmOfXn0mjJXLhcgMQAlrCUeAWrIyL2J_4JG9w8AGHV_2Mw6Ch3XEzq4Zv5L3PjBP7wFnbkVBGBl8dWSQ8SSTnei1XlQa_OwNWM-kTy6pehOKhnM8r9SfGXxWQdB0adyktpaMSYs4",
        "desc": "Làm việc tại Litva (Châu Âu) với vị trí nhân viên đóng gói. Cửa ngõ tuyệt vời để bước chân vào thị trường lao động Châu Âu với chi phí thấp, thủ tục nhanh chóng.",
        "tags": ["Lương từ 900 EUR/tháng", "Hợp đồng dài hạn", "Du lịch Schengen"],
        "modal": "litvaModal",
        "btnText": "Chi Tiết",
        "isHot": False,
        "icon": "luggage"
    },
    {
        "id": "portugal",
        "title": "Bồ Đào Nha",
        "image": "/assets/img/10-nu-don-dep-bdn.jpg",
        "desc": "Chương trình lao động Bồ Đào Nha ngành nhà hàng khách sạn. Công việc nhẹ nhàng, môi trường văn minh, thu nhập cao và là con đường ngắn nhất để có quốc tịch Châu Âu.",
        "tags": ["Thu nhập 40-50 triệu/tháng", "Công việc ổn định", "Lộ trình thẻ cư trú"],
        "modal": "portugalModal",
        "btnText": "Chi Tiết",
        "isHot": False,
        "icon": "restaurant"
    },
    {
        "id": "usa_j1",
        "title": "USA (J-1)",
        "image": "/public/assets/img/1787213884566_2187270042274317828_g925077470975449224_b4ce361e824088a98d357828bd5fb2c5.jpg",
        "desc": "Chương trình Giao lưu Văn hóa (J-1) mang đến cơ hội tuyệt vời để thanh niên trải nghiệm môi trường làm việc quốc tế, trau dồi tiếng Anh và khám phá văn hóa Hoa Kỳ.",
        "tags": ["Lương 14$ - 28$/giờ", "Trải nghiệm văn hóa Mỹ", "Nâng cao tiếng Anh"],
        "modal": "usaJ1Modal",
        "btnText": "Chi Tiết",
        "isHot": False,
        "icon": "school"
    },
    {
        "id": "usa_f1",
        "title": "Chuyển diện J-1 &rarr; F-1 (Du học Mỹ)",
        "image": "/public/assets/img/1787213884609_2187270042274317828_g925077470975449224_9c74e1e9b90188ffd5174e68e4ba6f57.jpg",
        "desc": "Giải pháp tối ưu dành cho ứng viên muốn chuyển đổi từ diện Giao lưu Văn hóa (J-1) sang diện Du học sinh (F-1) để tiếp tục con đường học vấn tại Mỹ hợp pháp, tiết kiệm.",
        "tags": ["Hợp pháp 100%", "An toàn, minh bạch", "Tối ưu hóa chi phí"],
        "modal": "usaF1Modal",
        "btnText": "Chi Tiết Phí",
        "isHot": False,
        "icon": "import_contacts"
    }
]

html_str = """<!-- Core Services Section -->
<section class="py-16 md:py-28 relative overflow-hidden bg-surface-container-lowest" id="programs">
    <!-- Phá cách: Decorative Abstract Backgrounds -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div class="absolute top-[5%] left-[-10%] w-[50vw] h-[50vw] bg-primary/10 rounded-full mix-blend-multiply filter blur-[120px] opacity-70 animate-[pulse_8s_ease-in-out_infinite]"></div>
        <div class="absolute top-[40%] right-[-10%] w-[40vw] h-[40vw] bg-secondary/10 rounded-full mix-blend-multiply filter blur-[100px] opacity-60 animate-[pulse_10s_ease-in-out_infinite_reverse]"></div>
        <div class="absolute bottom-[-10%] left-[20%] w-[60vw] h-[60vw] bg-primary/5 rounded-full mix-blend-multiply filter blur-[150px] opacity-50"></div>
        <!-- Thêm grid pattern mờ -->
        <div class="absolute inset-0 bg-[url('data:image/svg+xml,%3Csvg width=\\'60\\' height=\\'60\\' viewBox=\\'0 0 60 60\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cg fill=\\'none\\' fill-rule=\\'evenodd\\'%3E%3Cg fill=\\'%239C92AC\\' fill-opacity=\\'0.05\\'%3E%3Cpath d=\\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')] opacity-40"></div>
    </div>

    <div class="px-margin-mobile md:px-gutter max-w-container-max mx-auto relative z-10">

        <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start">

            <!-- Left Panel (Sticky) - 30% -->
            <div class="w-full lg:w-[30%] lg:sticky lg:top-32 flex flex-col justify-center pt-4 lg:pt-8">
                <div class="mb-8 lg:mb-0 relative">
                    <!-- Badge -->
                    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-surface text-primary font-bold text-sm mb-8 border border-primary/20 shadow-sm transform -rotate-2 hover:rotate-0 transition-transform duration-300">
                        <span class="material-symbols-outlined text-sm animate-pulse">public</span>
                        Khám Phá Thế Giới
                    </div>
                    
                    <h2 class="font-headline-lg text-4xl md:text-5xl lg:text-6xl text-on-surface mb-6 font-black leading-[1.1] tracking-tight relative z-10">
                        Hành Trình <br />
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary via-secondary to-primary bg-300% animate-gradient relative inline-block pb-2">
                            Kiến Tạo
                            <!-- Sparkle icon -->
                            <span class="material-symbols-outlined absolute -top-4 -right-8 text-secondary text-2xl animate-bounce">auto_awesome</span>
                        </span><br/>
                        Tương Lai
                    </h2>
                    
                    <p class="font-body-lg text-lg text-on-surface-variant leading-relaxed mb-10 relative z-10 border-l-4 border-primary/40 pl-4">
                        Lựa chọn lộ trình phù hợp nhất cho tương lai của bạn. Định cư, làm việc hay du học tại các quốc gia phát triển với sự đồng hành 100% từ Thanh Long.
                    </p>

                    <!-- Decorative elements -->
                    <div class="hidden lg:flex items-center gap-4">
                        <div class="w-16 h-16 rounded-full border-2 border-dashed border-primary/40 flex items-center justify-center animate-[spin_10s_linear_infinite]">
                            <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center">
                                <div class="w-2 h-2 rounded-full bg-primary"></div>
                            </div>
                        </div>
                        <div class="h-[2px] flex-1 bg-gradient-to-r from-primary/30 to-transparent"></div>
                    </div>
                </div>
            </div>

            <!-- Right Panel (Cards) - 70% -->
            <div class="w-full lg:w-[70%] flex flex-col gap-10 md:gap-16 relative">
                
                <!-- Timeline Line (Desktop only) -->
                <div class="hidden md:block absolute left-8 top-16 bottom-16 w-[3px] bg-gradient-to-b from-primary/40 via-secondary/40 to-transparent rounded-full shadow-[0_0_10px_rgba(var(--color-primary),0.3)]"></div>

"""

for i, item in enumerate(data):
    is_even = i % 2 == 1
    
    card_rounded = "md:rounded-tr-[4rem] md:rounded-bl-[4rem] md:rounded-tl-2xl md:rounded-br-2xl" if is_even else "md:rounded-tl-[4rem] md:rounded-br-[4rem] md:rounded-tr-2xl md:rounded-bl-2xl"
    img_rounded = "md:rounded-tr-[3rem] md:rounded-bl-xl md:rounded-tl-xl md:rounded-br-xl" if is_even else "md:rounded-tl-[3rem] md:rounded-br-xl md:rounded-tr-xl md:rounded-bl-xl"
    
    hot_badge = f'<span class="bg-error text-white px-3 py-1 rounded-full text-xs font-black tracking-wider shadow-lg animate-pulse border border-error/50">HOT</span>' if item["isHot"] else ""

    tags_html = ""
    for tag in item["tags"]:
        tags_html += f'<span class="inline-flex items-center gap-1.5 bg-surface text-on-surface px-3 py-1.5 rounded-xl text-sm font-semibold shadow-sm border border-outline-variant/30 hover:border-primary/50 transition-colors"><span class="material-symbols-outlined text-primary text-[18px]">check_circle</span> {tag}</span>\n                                '

    html_str += f"""
                <!-- ITEM {i+1}: {item["title"]} -->
                <div class="relative group pl-0 md:pl-24">
                    <!-- Timeline Dot -->
                    <div class="hidden md:flex absolute left-8 top-1/2 -translate-y-1/2 -translate-x-1/2 w-12 h-12 bg-surface-container-lowest rounded-full border-4 border-primary items-center justify-center z-10 shadow-[0_0_15px_rgba(0,0,0,0.1)] group-hover:scale-125 group-hover:border-secondary group-hover:shadow-[0_0_25px_rgba(var(--color-secondary),0.4)] transition-all duration-500">
                        <div class="w-4 h-4 bg-primary rounded-full group-hover:bg-secondary transition-colors duration-500"></div>
                    </div>

                    <!-- Card -->
                    <div class="bg-white/80 backdrop-blur-2xl rounded-[2rem] {card_rounded} overflow-hidden shadow-[0_8px_30px_rgba(0,0,0,0.06)] border border-white hover:border-primary/40 hover:shadow-[0_25px_60px_-15px_rgba(0,0,0,0.2)] transition-all duration-500 hover:-translate-y-2 flex flex-col sm:flex-row group/card">
                        
                        <div class="w-full sm:w-[45%] relative overflow-hidden p-3">
                            <div class="w-full h-full min-h-[250px] rounded-[1.5rem] {img_rounded} overflow-hidden relative group-hover/card:shadow-inner">
                                <img src="{item["image"]}"
                                    alt="{item["title"]}"
                                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 group-hover/card:scale-110">
                                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-80 group-hover/card:opacity-90 transition-opacity duration-300"></div>
                                <div class="absolute bottom-5 left-5 right-5 flex justify-between items-end">
                                    <h3 class="text-2xl md:text-3xl text-white font-black drop-shadow-md leading-tight">{item["title"]}</h3>
                                    {hot_badge}
                                </div>
                            </div>
                        </div>

                        <div class="p-6 sm:p-8 sm:w-[55%] flex flex-col justify-center relative">
                            <span class="material-symbols-outlined absolute top-4 right-4 text-7xl text-primary/5 -rotate-12 pointer-events-none font-light select-none group-hover/card:text-primary/10 transition-colors duration-500 group-hover/card:rotate-0">{item["icon"]}</span>
                            
                            <p class="text-on-surface-variant mb-6 flex-1 text-base leading-relaxed relative z-10">{item["desc"]}</p>
                            
                            <div class="flex flex-wrap gap-2 mb-8 relative z-10">
                                {tags_html}
                            </div>

                            <div class="mt-auto flex flex-col xl:flex-row gap-3 relative z-10">
                                <button onclick="openModal('{item["modal"]}')" class="flex-1 px-5 py-3 rounded-xl font-bold text-sm bg-surface text-primary border-2 border-primary/20 hover:border-primary hover:bg-primary/5 transition-all duration-300 group-hover/card:border-primary/50">{item["btnText"]}</button>
                                <button onclick="openModal('consultModal')" class="flex-1 px-5 py-3 rounded-xl font-bold text-sm bg-primary text-white hover:bg-primary-container hover:text-on-primary-container shadow-md hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden relative isolate after:content-[''] after:absolute after:inset-0 after:bg-white/20 after:translate-x-[-100%] hover:after:translate-x-[100%] after:transition-transform after:duration-700">Tư Vấn Ngay</button>
                            </div>
                        </div>
                    </div>
                </div>
"""

html_str += """
            </div>
        </div>
    </div>
</section>
"""

with open("/Users/khanhteu/Downloads/Workspace/stitch_business_showcase_landing_page/src/components/sections/programs.html", "w") as f:
    f.write(html_str)

