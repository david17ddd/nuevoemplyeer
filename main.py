from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.employee import Employee
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    employees = Employee.query.all()
    return render_template('dashboard.html', employees=employees)

@main_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        new_employee = Employee(name=name, position=position, salary=salary)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_employee.html')

@main_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.salary = request.form['salary']
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('edit_employee.html', employee=employee)

@main_bp.route('/delete/<int:id>')
@login_required
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('main.dashboard'))