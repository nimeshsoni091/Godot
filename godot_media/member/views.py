from django.shortcuts import render, redirect
from member.forms import MemberForm
from member.models import Members

# Create your views here.
from partner.models import Partners


def member_list(request, id):
    context = {'member_list': Members.objects.filter(partner=id),
               'partner_name': Partners.objects.get(pk=id).name,
               'partner_id': id}
    return render(request, "member_list.html", context)


def member_form(request, pid=0, id=0):
    # we are calling same function for GET and POST request
    partner_name = Partners.objects.get(pk=pid).name
    if request.method == "GET":
        if id == 0:  # determines insert operation
            form = MemberForm()
            operation = "insert"
        else:  # determines update operation and populate pre filled form
            member = Members.objects.get(pk=id)
            form = MemberForm(instance=member)
            operation = "update"
        return render(request, "member_form.html", {'form': form, 'partner_name': partner_name, 'partner_id': pid,
                                                    'operation': operation})
    else:
        if id == 0:  # this indicates create operation
            form = MemberForm(request.POST)
        else:  # this indicates update operation
            member = Members.objects.get(pk=id)
            form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            # handling partner object during form submit
            try:
                form.save()
            except:
                obj = form.save(commit=False)
                obj.partner = Partners.objects.get(pk=pid)
                obj.save()

        return redirect('/member/list/' + str(pid))


def member_delete(request, id):
    member = Members.objects.get(pk=id)
    member.delete()
    return redirect('/member/list/' + str(member.partner.id))
