# Godot 4.x Scene Tree & Node Architecture Reference

This reference guides AI agents when inspecting, creating, or editing text-based Godot `.tscn` scene files, node trees, and GDScript bindings.

## Text-Based `.tscn` File Anatomy

Godot 4.x scene files are plain-text formats using TOML-like key-value structures.

```toml
[gd_scene load_steps=3 format=3 uid="uid://example_uid"]

[ext_resource type="Script" path="res://scripts/player.gd" id="1_script"]
[ext_resource type="Texture2D" path="res://assets/player_sprite.png" id="2_texture"]

[node name="Player" type="CharacterBody2D"]
script = ExtResource("1_script")

[node name="Sprite2D" type="Sprite2D" parent="."]
texture = ExtResource("2_texture")
hframes = 6
vframes = 6

[node name="CollisionShape2D" type="CollisionShape2D" parent="."]
```

## Node Rules for AI Agents

1. **Root Node**: Must match the intended scene type (e.g. `CharacterBody2D` for physics players, `Control` for UI overlays, `Node2D` for world objects).
2. **Parent Designation**:
   - `parent="."` designates a direct child of the root node.
   - `parent="Sprite2D"` designates a child of the `Sprite2D` sub-node.
3. **Signal Connections**:
   - Signal connections appear at the end of `.tscn` files under `[connection]` headers:
     ```toml
     [connection signal="pressed" from="BuildButton" to="." method="_on_build_button_pressed"]
     ```

## Headless Verification

Always verify scene validity using Godot CLI headless execution:

```powershell
godot --headless --quit-after 5
```
