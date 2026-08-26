import re
import sys

def main():
    file_path = '/Users/khanhteu/Downloads/Workspace/stitch_business_showcase_landing_page/code.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Canada button
    content = content.replace('onclick="openCanadaModal()"', 'onclick="openModal(\'canadaModal\')"')
    
    # 2. Update Ireland button
    ireland_target = '''                        <a class="mt-auto block text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors"
                            href="#contact">Tìm Hiểu Thêm</a>'''
    ireland_replacement = '''                        <div class="mt-auto flex gap-2">
                            <button onclick="openModal('irelandModal')" class="flex-1 text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors shadow-sm border border-outline-variant">Chi Tiết</button>
                            <a class="flex-1 block text-center w-full bg-primary text-on-primary py-2.5 rounded-lg font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-md"
                                href="#contact">Tư Vấn Ngay</a>
                        </div>'''
    content = content.replace(ireland_target, ireland_replacement)
    
    # 3. Update USA button
    usa_target = '''                        <a class="mt-auto block text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors"
                            href="#contact">Chi Tiết</a>'''
    usa_replacement = '''                        <div class="mt-auto flex gap-2">
                            <button onclick="openModal('usaModal')" class="flex-1 text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors shadow-sm border border-outline-variant">Chi Tiết</button>
                            <a class="flex-1 block text-center w-full bg-primary text-on-primary py-2.5 rounded-lg font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-md"
                                href="#contact">Tư Vấn Ngay</a>
                        </div>'''
    content = content.replace(usa_target, usa_replacement)
    
    # 4. Update Litva button
    litva_target = '''                        <a class="mt-auto block text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors"
                            href="#contact">Xem Ngay</a>'''
    litva_replacement = '''                        <div class="mt-auto flex gap-2">
                            <button onclick="openModal('litvaModal')" class="flex-1 text-center w-full bg-surface-container text-primary py-2.5 rounded-lg font-label-bold hover:bg-primary/10 transition-colors shadow-sm border border-outline-variant">Chi Tiết</button>
                            <a class="flex-1 block text-center w-full bg-primary text-on-primary py-2.5 rounded-lg font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-md"
                                href="#contact">Tư Vấn Ngay</a>
                        </div>'''
    content = content.replace(litva_target, litva_replacement)

    # 5. Fix Canada close buttons
    content = content.replace('onclick="closeCanadaModal()"', 'onclick="closeModal(\'canadaModal\')"')

    # 6. Add modals HTML
    modals_html = """
    <!-- Ireland Job Modal -->
    <div id="irelandModal" class="modal-backdrop fixed inset-0 z-[100] hidden items-center justify-center bg-ink-black/60 backdrop-blur-sm p-4 opacity-0 transition-opacity duration-300">
        <div class="modal-content bg-surface-container-lowest rounded-3xl w-full max-w-3xl max-h-[90vh] overflow-y-auto shadow-2xl transform scale-95 transition-transform duration-300">
            <div class="sticky top-0 bg-surface-container-lowest border-b border-outline-variant p-6 flex justify-between items-center z-10">
                <div>
                    <h3 class="font-headline-md text-primary font-bold text-xl md:text-2xl">THÔNG BÁO ĐƠN HÀNG</h3>
                    <p class="text-secondary font-bold text-sm md:text-base uppercase">Chương trình hái nấm Ireland</p>
                </div>
                <button onclick="closeModal('irelandModal')" class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-surface-container-high text-on-surface-variant transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="p-6">
                <div class="overflow-x-auto rounded-xl border border-outline-variant">
                    <table class="w-full text-left border-collapse min-w-[600px]">
                        <thead>
                            <tr class="bg-success-green-light border-b border-outline-variant">
                                <th class="p-3 font-bold text-tertiary-container w-1/3 border-r border-outline-variant">Hạng mục</th>
                                <th class="p-3 font-bold text-tertiary-container">Nội dung</th>
                            </tr>
                        </thead>
                        <tbody class="text-on-surface-variant text-sm md:text-base divide-y divide-outline-variant">
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Công việc tiếp nhận:</td>
                                <td class="p-3 font-bold text-primary">NÔNG NGHIỆP (HÁI NẤM)</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Địa điểm làm việc:</td>
                                <td class="p-3 font-bold text-primary">IRELAND</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Điều kiện tuyển dụng:</td>
                                <td class="p-3">Sức khỏe tốt, chăm chỉ, không yêu cầu kinh nghiệm</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Thu nhập:</td>
                                <td class="p-3 font-bold text-error">~ 14 EUR / giờ</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Quyền lợi:</td>
                                <td class="p-3 font-bold text-error">Môi trường làm việc an toàn, ổn định lâu dài tại Châu Âu</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-6 border-t border-outline-variant bg-surface-container-low flex justify-end gap-4 rounded-b-3xl">
                <button onclick="closeModal('irelandModal')" class="px-6 py-2.5 rounded-full font-label-bold text-primary hover:bg-primary/10 transition-colors border border-outline-variant bg-surface-container-lowest">Đóng</button>
                <a href="#contact" onclick="closeModal('irelandModal')" class="bg-primary text-on-primary px-8 py-2.5 rounded-full font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-sm">Đăng Ký Tư Vấn</a>
            </div>
        </div>
    </div>

    <!-- USA Job Modal -->
    <div id="usaModal" class="modal-backdrop fixed inset-0 z-[100] hidden items-center justify-center bg-ink-black/60 backdrop-blur-sm p-4 opacity-0 transition-opacity duration-300">
        <div class="modal-content bg-surface-container-lowest rounded-3xl w-full max-w-3xl max-h-[90vh] overflow-y-auto shadow-2xl transform scale-95 transition-transform duration-300">
            <div class="sticky top-0 bg-surface-container-lowest border-b border-outline-variant p-6 flex justify-between items-center z-10">
                <div>
                    <h3 class="font-headline-md text-primary font-bold text-xl md:text-2xl">THÔNG BÁO ĐƠN HÀNG</h3>
                    <p class="text-secondary font-bold text-sm md:text-base uppercase">Định cư Mỹ diện lao động phổ thông (EB-3)</p>
                </div>
                <button onclick="closeModal('usaModal')" class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-surface-container-high text-on-surface-variant transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="p-6">
                <div class="overflow-x-auto rounded-xl border border-outline-variant">
                    <table class="w-full text-left border-collapse min-w-[600px]">
                        <thead>
                            <tr class="bg-success-green-light border-b border-outline-variant">
                                <th class="p-3 font-bold text-tertiary-container w-1/3 border-r border-outline-variant">Hạng mục</th>
                                <th class="p-3 font-bold text-tertiary-container">Nội dung</th>
                            </tr>
                        </thead>
                        <tbody class="text-on-surface-variant text-sm md:text-base divide-y divide-outline-variant">
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Công việc tiếp nhận:</td>
                                <td class="p-3 font-bold text-primary">LAO ĐỘNG PHỔ THÔNG (Nhà máy đóng gói, chế biến...)</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Địa điểm làm việc:</td>
                                <td class="p-3 font-bold text-primary">USA (HOA KỲ)</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Điều kiện tuyển dụng:</td>
                                <td class="p-3">Không yêu cầu kinh nghiệm, bằng cấp. Đủ sức khỏe lao động.</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Quyền lợi đặc biệt:</td>
                                <td class="p-3 font-bold text-error">Được cấp Thẻ Xanh (Green Card) cho cả gia đình</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Lợi ích cho người phụ thuộc:</td>
                                <td class="p-3 font-bold">Vợ/chồng được đi làm tự do, con cái học miễn phí đến lớp 12</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-6 border-t border-outline-variant bg-surface-container-low flex justify-end gap-4 rounded-b-3xl">
                <button onclick="closeModal('usaModal')" class="px-6 py-2.5 rounded-full font-label-bold text-primary hover:bg-primary/10 transition-colors border border-outline-variant bg-surface-container-lowest">Đóng</button>
                <a href="#contact" onclick="closeModal('usaModal')" class="bg-primary text-on-primary px-8 py-2.5 rounded-full font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-sm">Đăng Ký Tư Vấn</a>
            </div>
        </div>
    </div>

    <!-- Litva Job Modal -->
    <div id="litvaModal" class="modal-backdrop fixed inset-0 z-[100] hidden items-center justify-center bg-ink-black/60 backdrop-blur-sm p-4 opacity-0 transition-opacity duration-300">
        <div class="modal-content bg-surface-container-lowest rounded-3xl w-full max-w-3xl max-h-[90vh] overflow-y-auto shadow-2xl transform scale-95 transition-transform duration-300">
            <div class="sticky top-0 bg-surface-container-lowest border-b border-outline-variant p-6 flex justify-between items-center z-10">
                <div>
                    <h3 class="font-headline-md text-primary font-bold text-xl md:text-2xl">THÔNG BÁO ĐƠN HÀNG</h3>
                    <p class="text-secondary font-bold text-sm md:text-base uppercase">Nhân viên đóng gói (Packer) tại Litva</p>
                </div>
                <button onclick="closeModal('litvaModal')" class="w-10 h-10 flex items-center justify-center rounded-full hover:bg-surface-container-high text-on-surface-variant transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="p-6">
                <div class="overflow-x-auto rounded-xl border border-outline-variant">
                    <table class="w-full text-left border-collapse min-w-[600px]">
                        <thead>
                            <tr class="bg-success-green-light border-b border-outline-variant">
                                <th class="p-3 font-bold text-tertiary-container w-1/3 border-r border-outline-variant">Hạng mục</th>
                                <th class="p-3 font-bold text-tertiary-container">Nội dung</th>
                            </tr>
                        </thead>
                        <tbody class="text-on-surface-variant text-sm md:text-base divide-y divide-outline-variant">
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Công việc tiếp nhận:</td>
                                <td class="p-3 font-bold text-primary">NHÂN VIÊN ĐÓNG GÓI (PACKER)</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Địa điểm làm việc:</td>
                                <td class="p-3 font-bold text-primary">LITVA (CHÂU ÂU)</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Yêu cầu tiếng:</td>
                                <td class="p-3 text-error">Tiếng Anh giao tiếp cơ bản</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Thu nhập:</td>
                                <td class="p-3 font-bold text-error">Từ 900 EUR Net / tháng</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-bold border-r border-outline-variant">Môi trường:</td>
                                <td class="p-3 font-bold">Làm việc trong trung tâm logistic sạch sẽ, hiện đại</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-6 border-t border-outline-variant bg-surface-container-low flex justify-end gap-4 rounded-b-3xl">
                <button onclick="closeModal('litvaModal')" class="px-6 py-2.5 rounded-full font-label-bold text-primary hover:bg-primary/10 transition-colors border border-outline-variant bg-surface-container-lowest">Đóng</button>
                <a href="#contact" onclick="closeModal('litvaModal')" class="bg-primary text-on-primary px-8 py-2.5 rounded-full font-label-bold hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-sm">Đăng Ký Tư Vấn</a>
            </div>
        </div>
    </div>
"""

    script_target = '''    <script>
        const canadaModal = document.getElementById('canadaModal');
        const canadaModalContent = document.getElementById('canadaModalContent');

        function openCanadaModal() {
            canadaModal.classList.remove('hidden');
            canadaModal.classList.add('flex');
            // Delay for animation
            setTimeout(() => {
                canadaModal.classList.remove('opacity-0');
                canadaModalContent.classList.remove('scale-95');
                canadaModalContent.classList.add('scale-100');
            }, 10);
            document.body.style.overflow = 'hidden';
        }

        function closeCanadaModal() {
            canadaModal.classList.add('opacity-0');
            canadaModalContent.classList.remove('scale-100');
            canadaModalContent.classList.add('scale-95');
            setTimeout(() => {
                canadaModal.classList.add('hidden');
                canadaModal.classList.remove('flex');
                document.body.style.overflow = '';
            }, 300);
        }

        canadaModal.addEventListener('click', (e) => {
            if (e.target === canadaModal) {
                closeCanadaModal();
            }
        });
    </script>'''

    unified_script = '''    <script>
        function openModal(modalId) {
            const modal = document.getElementById(modalId);
            const modalContent = modal.querySelector('div[id$="ModalContent"]') || modal.querySelector('.modal-content');
            
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            // Delay for animation
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                if (modalContent) {
                    modalContent.classList.remove('scale-95');
                    modalContent.classList.add('scale-100');
                }
            }, 10);
            document.body.style.overflow = 'hidden';
        }

        function closeModal(modalId) {
            const modal = document.getElementById(modalId);
            const modalContent = modal.querySelector('div[id$="ModalContent"]') || modal.querySelector('.modal-content');
            
            modal.classList.add('opacity-0');
            if (modalContent) {
                modalContent.classList.remove('scale-100');
                modalContent.classList.add('scale-95');
            }
            setTimeout(() => {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                document.body.style.overflow = '';
            }, 300);
        }

        // Add event listeners for clicking outside modals
        document.querySelectorAll('div[id$="Modal"]').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeModal(modal.id);
                }
            });
        });
    </script>'''

    content = content.replace(script_target, modals_html + '\\n' + unified_script)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
