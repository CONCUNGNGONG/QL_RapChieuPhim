import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host="localhost",  # Thay bằng host của bạn
    database="ticket_manager",  # Thay bằng tên database của bạn
    user="root",  # Thay bằng tên người dùng của bạn
    password=""  # Thay bằng mật khẩu của bạn
)

# Truy vấn dữ liệu từ cơ sở dữ liệu
query = """
SELECT 
    t.id AS ticket_id,
    t.idCalendar,
    t.name AS customer_name,
    t.numPerson,
    t.numPopcorn,
    t.numWater,
    t.priceTicket,
    staff.name AS staff_name, 
    t.createAt,
    seat.location AS seat_location
FROM ticket t
LEFT JOIN seat ON t.id = seat.idTicket
LEFT JOIN staff ON t.createBy = staff.idnv;
"""
data = pd.read_sql(query, con=conn)

# Tính toán cần thiết
## Thêm các giá trị tính toán phụ thuộc
# Giả sử dụng giá trị mặc định cho pricePopcorn và priceWater do cột này không tồn tại trong database
price_popcorn = 50000  # Giá mỗ ngô
price_water = 20000  # Giá nước

data['total_spent'] = (
    data['numPerson'] * data['priceTicket'] +
    data['numPopcorn'] * price_popcorn +
    data['numWater'] * price_water
)

## Tổng doanh thu theo lịch chiếu
data['total_revenue'] = data['total_spent']

## Xử lý idCalendar và chuyển sang thời gian cụ thể
# Tách phần timestamp từ idCalendar
data['calendar_timestamp'] = data['idCalendar'].str.extract(r'CALENDAR_(\d+)_')[0].astype(float)
data['calendar_time'] = pd.to_datetime(data['calendar_timestamp'], unit='s')

## Top nhân viên đóng góp nhiều nhất
top_employees = data['staff_name'].value_counts().head(5)

## Top khách hàng chi tiêu nhiều nhất
top_customers = data.groupby('customer_name')['total_spent'].sum().nlargest(5)

## Top lịch chiếu có doanh thu cao nhất
movie_revenue = data.groupby('calendar_time')['total_revenue'].sum().nlargest(5)

## Doanh thu theo thời gian (ngày/tháng/năm)
data['createAt'] = pd.to_datetime(data['createAt'], unit='s')
date_revenue = data.groupby(data['createAt'].dt.date)['total_revenue'].sum()

# Trực quan hóa dữ liệu
plt.figure(figsize=(20, 10))

# Biểu đồ tròn: Top nhân viên đóng góp nhiều nhất
plt.subplot(2, 2, 1)
colors_employees = sns.color_palette('viridis', len(top_employees))
top_employees.plot.pie(
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors_employees,
    legend=False
)
plt.title('Top Nhân Viên Đóng Góp Nhiều Nhất')
plt.ylabel('')

# Biểu đồ tròn: Top khách hàng chi tiêu nhiều nhất
plt.subplot(2, 2, 2)
colors_customers = sns.color_palette('plasma', len(top_customers))
top_customers.plot.pie(
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors_customers,
    legend=False
)
plt.title('Top Khách Hàng Chi Tiêu Nhiều Nhất')
plt.ylabel('')

# Thêm legend cho "Top khách hàng chi tiêu nhiều nhất"
plt.legend(
    top_customers.index, 
    loc="center left", 
    bbox_to_anchor=(1.1, 0.5), 
    title="Khách Hàng"
)

# Biểu đồ cột: Top lịch chiếu doanh thu cao nhất
plt.subplot(2, 2, 3)
movie_revenue.plot(kind='bar', color='skyblue')
plt.title('Top Lịch Chiếu Doanh Thu Cao Nhất')
plt.xlabel('Thời Gian Lịch Chiếu')
plt.ylabel('Doanh Thu (VNĐ)')
plt.xticks(rotation=45)

# Biểu đồ đường: Doanh thu theo thời gian
plt.subplot(2, 2, 4)
date_revenue.plot(kind='line', marker='o', color='green')
plt.title('Doanh Thu Theo Thời Gian')
plt.xlabel('Ngày')
plt.ylabel('Doanh Thu (triệu VNĐ)')
plt.xticks(rotation=45)

# Sắp xếp lại layout để không bị chồng chéo
plt.tight_layout()
plt.show()

# Đóng kết nối
conn.close()
