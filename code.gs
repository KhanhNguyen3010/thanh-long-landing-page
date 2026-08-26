function doPost(e) {
  try {
    var data = e.parameter;
    
    // Nếu có truyền sheetId từ form lên, thì mở sheet đó. Nếu không thì dùng sheet mặc định (chứa script)
    var sheet;
    if (data.sheetId) {
      sheet = SpreadsheetApp.openById(data.sheetId).getActiveSheet();
    } else {
      sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    }
    
    // Kiểm tra xem sheet đã có tiêu đề chưa, nếu chưa thì tự tạo
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Timestamp", "Họ Tên", "Số ĐT", "Email", "Chương trình", "Lời nhắn"]);
      sheet.getRange("A1:F1").setFontWeight("bold").setBackground("#f3f4f6");
    }


    // Thêm thời gian
    var timestamp = new Date();
    
    // Lấy các trường dữ liệu từ form (khớp với thuộc tính 'name' trong HTML)
    var name = data.name || "";
    var phone = data.phone ? "'" + data.phone : "";
    var email = data.email || "";
    var program = data.program || "";
    var notes = data.notes || "";
    
    // Thêm 1 dòng mới vào Google Sheet
    sheet.appendRow([timestamp, name, phone, email, program, notes]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ "result": "success" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ "result": "error", "error": error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
