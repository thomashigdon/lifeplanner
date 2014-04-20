from datetime import datetime
from django.db import models
from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    task = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True,)
    finished_time = models.DateTimeField(default=None)

    ordering = ['finished', 'task' ]

    def __unicode__(self):
        return '%s' % self.task

    def make_finished(self):
        if not self.is_leaf():
            return
        self.finished = True
        self.finished_time = datetime.now()
        self.save()
        ancestors = self.get_ancestors().reverse()
        for ancestor in ancestors:
            finished_list = [ x.finished for x in ancestor.get_children() ]
            if reduce(lambda x,y: x and y, finished_list):
                ancestor.finished = True
                ancestor.finished_time = datetime.now()
                ancestor.save()
            else:
                return

    def make_unfinished(self):
        if not self.is_leaf():
            return
        self.finished = False
        self.save()
        ancestors = self.get_ancestors()
        for ancestor in ancestors:
            ancestor.finished = False
            ancestor.save()

    def get_children(self, filter={}):
        return MP_Node.get_children(self).filter(**filter)
