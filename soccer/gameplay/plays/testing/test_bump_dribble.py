import play
import behavior
import skills.bump_dribble
import robocup
import main


class TestBumpDribble(play.Play):
    def __init__(self):
        super().__init__(continuous=True)
        self.add_transition(behavior.Behavior.State.start,
                            behavior.Behavior.State.running, lambda: True,
                            "immediately")

    def on_enter_running(self):
        b = skills.bump_dribble.BumpDribble(robocup.Point(0,0))
        self.add_subbehavior(b, name='dribble', required=True)

    def on_exit_running(self):
        self.remove_subbehavior('dribble')
