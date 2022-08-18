from tasks.models import Task


def processors(request):
    is_boss = request.user.groups.filter(name="boss").exists()

    not_seen_task = Task.objects.filter(assigned_user=request.user,is_seen=False)

    return {
        'is_boss_process': is_boss,
        'not_seen_task':not_seen_task
    }
