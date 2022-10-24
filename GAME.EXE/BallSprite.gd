extends KinematicBody2D

export (int) var speed = 200

var velocity = Vector2()


func get_input():
	velocity = Vector2()
	
	velocity.x -= 1
	
	velocity = velocity.normalized() * speed

func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)
	var collision = move_and_collide(velocity * delta)
	if move_and_collide(velocity * delta) == KinematicBody2D:
		print("Enimy Spotted")
