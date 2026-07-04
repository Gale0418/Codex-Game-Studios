# AI Game Asset Pipeline Reference

Guidelines for integrating AI-generated 2D sprites, sprite sheets, transparent backgrounds, and audio assets into game projects.

## 2D Sprite Sheet & Video Keying

For AI-generated video or sprite sheets (e.g. ComfyUI, Stable Diffusion):

1. **Background Removal**:
   - Use `Background_remover` (`npm run dev` at `http://localhost:5177`) to key solid/green backgrounds and produce transparent PNG sheets + `metadata.json`.
2. **Metadata Fields**:
   - `frameRect`: Exact ROI for Godot AtlasTexture / Region.
   - `extrude`: Edge padding (recommended `extrude: 1`, `padding: 2`) to prevent texture bleeding across grid boundaries.
3. **Godot AtlasTexture Integration**:
   - Map a 6x6 sheet into Godot via `AtlasTexture` in GDScript:
     ```gdscript
     var atlas = AtlasTexture.new()
     atlas.atlas = preload("res://assets/sheet.png")
     atlas.region = Rect2(col * 64, row * 64, 64, 64)
     ```

## Audio & Sound Effects Pipeline

- **Sfx / Music Format**: Convert WAV/MP3 to OGG Vorbis (`.ogg`) for loopable background music and `.wav` for low-latency sound effects.
