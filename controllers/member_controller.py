from flask import render_template, redirect, request
from flask import Blueprint

from models.member import Member

import repositories.member_repo as member_repo
import repositories.admin_repo as admin_repo

members_blueprint = Blueprint('members', __name__)

# READ - GET - Show All
@members_blueprint.route('/members', methods=['GET'])
def all_members():
    members = member_repo.select_all()
    header = 'All Members'
    return render_template('members/index.html', members=members, header=header)

# READ - GET - Show All Active
@members_blueprint.route('/members/active', methods=['GET'])
def all_active_members():
    members = member_repo.select_all_active()
    header = 'All Active Members'
    return render_template('members/index.html', members=members, header=header)

# READ - GET - Show All Inactive
@members_blueprint.route('/members/inactive', methods=['GET'])
def all_inactive_members():
    members = member_repo.select_all_active(active=False)
    header = 'All Inactive Members'
    return render_template('members/index.html', members=members, header=header)

# READ - Show One
@members_blueprint.route('/members/<int:id>', methods=['GET'])
def one_member(id):
    member = member_repo.select(id)
    classes = admin_repo.get_all_booked_classes(member.id)
    return render_template('members/show.html', member = member, classes = classes)

# CREATE - GET - Show form
@members_blueprint.route('/members/new', methods=['GET'])
def create_member_form():
    return render_template('members/new.html')

# CREATE - POST - Process request
@members_blueprint.route('/members/new', methods=['POST'])
def create_member_save():
    form_data = request.form
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    is_premium = 'premium' in form_data
    is_active = 'active' in form_data
    member = Member(first_name, last_name, is_premium, is_active)
    member = member_repo.save(member)
    return redirect(f'/members/{member.id}')

# EDIT - GET - Show form
@members_blueprint.route('/members/<int:id>/edit', methods=['GET'])
def one_member_edit_show(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member = member)

# EDIT - POST - Process request
@members_blueprint.route('/members/<int:id>/edit', methods=['POST'])
def one_member_edit_save(id):
    form_data = request.form
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    is_premium = 'premium' in form_data
    is_active = 'active' in form_data
    member = Member(first_name, last_name, is_premium, is_active, id)
    member_repo.update(member)
    return redirect(f'/members/{id}')

# DELETE - POST - Process request
@members_blueprint.route('/members/<int:id>/delete', methods=['GET'])
def one_member_delete(id):
    member_repo.delete(id)
    return redirect('/members')

# EDIT - GET - Toggle Active/Inactive
@members_blueprint.route('/members/<int:id>/toggle', methods=['GET'])
def toggle_active(id):
    member = member_repo.select(id)
    member.is_active = not member.is_active
    member = member_repo.update(member)
    return redirect(request.referrer)