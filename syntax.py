# syntax.py

import sys

from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

def format(color, style=''):
    """Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages
STYLES = {
    'keyword': format('#8ABEB7', 'bold'),
    'operator': format('#CC6666', 'bold'),
    'brace': format('#DE935F', 'bold'),
    'defclass': format('#C5C8C6', 'bold'),
    'string': format('#CC6666'),
    'string2': format('#B294BB'),
    'comment': format('#969896', 'italic'),
    'self': format('#81A2BE', 'italic'),
    'numbers': format('#73EC0F'),
}


class PythonHighlighter (QSyntaxHighlighter):
    """Syntax highlighter for the Python language.
    """
    # Python keywords
    keywords = [
        'bind', 'alias', 'echo', 'exec', 'say', 'sat_team',
    ]

    # Python operators
    operators = [
        # CVARS
        'cl_', 'mp_', 'sv_', 'mat_', 'r_', 'm_', 'net_', 'hud_','overview_','replay_','youtube_','spec_','voice_',
        #'addip', 'adsp_alley_min', 'adsp_courtyard_min', 'adsp_debug', 'adsp_door_height', 'adsp_duct_min', 'adsp_hal_min', 'adsp_low_ceiling', 'adsp_opencourtyard_min', 'adsp_openspace_min', 'adsp_openstreet_min', 'adsp_openwall_min', 'adsp_room_min', 'adp_street_min', 'adsp_tunnel_min', 'adsp_wall_height', 'ai_auto_contact_solver', 'ai_clear_bad_links', 'ai_debug_assault', 'ai_debug_diretnavprobe', 'ai_debug_doors', 'ai_debug_efficiency', 'ai_debug_enemies', 'ai_debug_expressions', 'ai_debug_follow', 'ai_debug_loners', 'ai_debug_looktargets', 'ai_debug_los', 'ai_debug_nav', 'ai_debug_node_connect', 'ai_debg_ragdoll_magnets', 'ai_debug_shoot_positions', 'ai_debug_speech', 'ai_debug_squads', 'ai_debug_think_ticks', 'ai_debugscriptconditions', 'ai_disable', 'ai_drawbattlelines', 'ai_dump_hints', 'ai_efficiency_override', 'ai_follow_use_points', 'ai_follow_use_points_when_moving', 'ai_lead_tme', 'ai_LOS_mode', 'ai_moveprobe_debug', 'ai_moveprobe_jump_debug', 'ai_moveprobe_usetracelist', 'ai_next_hull', 'ai_no_local_paths', 'ai_no_node_cache', 'ai_no_select_box', 'ai_no_steer', 'ai_no_talk_delay', 'ai_nodes', 'ai_norebuildgraph', 'ai_path_adjust_speed_on_immediate_turns', 'ai_path_insert_pause_at_est_end', 'ai_path_insert_pause_at_obstruction', 'ai_reaction_delay_alert', 'ai_reaction_delay_idle', 'ai_rebalance_thinks', 'ai_reloadresponsesystems', 'ai_report_task_timings_on_limit', 'ai_resume', 'ai_sequence_debug', 'ai_set_move_height_epsilon', 'ai_shot_bias', 'ai_shot_bias_max', 'ai_shot_bias_min', 'ai_shot_stats', 'ai_shot_stats_term', 'ai_show_connect', 'ai_show_connect_fly', 'ai_show_connect_jump', 'ai_show_graph_connect', 'ai_show_grid', 'ai_show_hints', 'ai_show_hull', 'ai_show_hull_attacks', 'ai_show_node', 'ai_show_think_tolerance', 'ai_show_visibility', 'ai_simulate_task_overtime', 'ai_spread_cone_focus_time', 'ai_spread_defocused_cone_multiplier', 'ai_spread_pattern_focus_time', 'ai_step', 'ai_think_limit_label', 'ai_use_clipped_paths', 'ai_use_efficiency', 'ai_use_frame_think_limits', 'ai_use_think_optimizations', 'ainet_generate_report', 'ainet_generate_report_only', 'air_density', 'alias', 'ammo_38mag_max', 'ammo_357sig_max', 'ammo_45acp_max', 'ammo_50AE_max', 'ammo_556mm_box_max', 'ammo_556mm_max', 'ammo_57mm_max', 'ammo_762mm_max', 'ammo_9mm_max', 'ammo_buckshot_max', 'ammo_flashbang_max', 'ammo_hegrenade_max', 'ammo_smokegrenade_max', 'async_mode', 'async_simulate_delay', 'async_simulate_mixed_mode', 'autobuy', 'autosave', 'banid', 'banip', 'bench_end', 'bench_showstatsdialog', 'bench_start', 'bench_upload', 'benchframe', 'bgmvolume', 'bind', 'BindToggle', 'blink_duration', 'bloodspray', 'bot_add', 'bot_add_ct', 'bot_add_t', 'bot_all_weapons', 'bot_allow_grenades', 'bot_allo_machine_guns', 'bot_allow_pistols', 'bot_allow_rifles', 'bot_allow_rogues', 'bot_allw_shotguns', 'bot_allow_snipers', 'bot_allow_sub_machine_guns', 'bot_auto_follow', 'bot_auto_vacate', 'bot_chatter', 'bot_crouch', 'bot_debug', 'bot_debug_target', 'bot_defer_to_human', 'bot_difficulty', 'bot_dont_shoot', 'bot_freeze', 'bot_goto_mark', 'bot_join_after_player', 'botjoin_team', 'bot_kick', 'bot_kill', 'bo_knives_only', 'bot_loadout', 'bot_mimic', 'bot_mimic_yaw_offset', 'bot_pistols_only', 'bot_prefix', 'bot_profile_db', 'bot_quota', 'bot_quota_mode', 'bot_show_battlefront', 'bot_show_nav', 'bot_show_occupy_time', 'bot_snipers_only', 'bot_stop', 'bot_traceview', 'bot_walk', 'bot_zombie', 'box', 'breakable_disable_gib_limit', 'breakable_multiplayer', 'buddha', 'budget_averages_window', 'budget_background_alpha', 'budget_bargraph_background_alpha', 'budget_bargraph_range_ms', 'budget_history_numsamplesvisible', 'budget_history_range_ms', 'budget_panel_bottom_of_history_fraction', 'budget_panel_height', 'budget_panel_width', 'budget_panel_x', 'budget_panel_y', 'budget_peaks_window', 'budget_show_averages', 'udget_show_history', 'budget_show_peaks', 'bug', 'bug_swap', 'bugreporter_inludebsp', 'buildcubemaps', 'building_cubemaps', 'buyequip', 'buymenu', 'c_maxdistance', 'c_maxpitch', 'c_maxyaw', 'c_mindistance', 'c_minpitch', 'c_minyaw', 'c_orthoheight', 'c_orthowidth', 'cache_print', 'cache_print_lru', 'cache_print_summary', 'cache_set_print_section', 'cam_command', 'cam_idealdist', 'cam_idealpitch', 'cam_idealyaw', 'cam_snapto', 'camortho', 'cancelselect', 'cast_hull', 'cast_ray', 'cc_captiontrace', 'cc_emit', 'cc_lang', 'cc_linger_time', 'cc_lookup_crc', 'cc_predisplay_time', 'cc_sentencecaptionnorepeat', 'cc_subtitles', 'cd', 'centerview', 'ch_createairboat', 'ch_createjeep', 'changelevel', 'changelevel2', 'chooseteam', 'cl_allowdownload', 'cl_allowupload', 'cl_anglespeedkey', 'cl_animationinfo', 'cl_autobuy', 'cl_autohelp', 'cl_autowepswitch', 'cl_backspeed', 'cl_bob', 'cl_bobcycle', 'cl_bobup', 'cl_buy_favorite', 'cl_buy_favorite_nowarn', 'cl_buy_favorite_quiet', 'cl_buy_favorite_reset', 'cl_c4dynamiclight', 'cl_c4progressbar', 'cl_class', 'cl_clock_correction', 'cl_clock_correction_adjustment_max_amount', 'cl_clock_correction_adjustment_max_offset', 'cl_clock_correction_adjustment_min_offset', 'cl_clock_correction_force_server_tick', 'cl_clock_showdebuginfo', 'cl_clockdrift_max_ms', 'cl_cmdbackup', 'cl_cmdrate', 'cl_crosshairalpha', 'cl_crosshaircolor', 'cl_crosshairscale', 'cl_crosshairusealpha', 'cl_customsounds', 'cl_demoviewoverride', 'cl_detaildist', 'cl_detailfade', 'cl_downloadfilter', 'cl_drawhud', 'cl_drawleaf', 'cl_drawmaterial', 'cl_drawmonitors', 'cl_drawshadowtexture', 'cl_dynamiccrosshair', 'cl_ejectbrass', 'cl_ent_absbox', 'cl_ent_bbox', 'cl_ent_rbox', 'cl_entityreport', 'cl_extrapolate', 'cl_extrapolate_amount', 'cl_flushentitypacket', 'cl_forcehighendmonitors', 'cl_forcepreload', 'cl_forwardspeed', 'cl_fullupdate', 'cl_idealpitchscale', 'cl_ignorepackets', 'cl_interp', 'cl_interp_npcs', 'cl_interpolate', 'cl_lagcomp_errorcheck', 'cl_lagcompensation', 'cl_left_hand_ik', 'cl_leveloverview', 'cl_leveloverviewmarker', 'cl_localnetworkbackdoor', 'cl_locationalpha', 'cl_logofile', 'cl_maxrenderable_dist', 'cl_mouseenable', 'cl_mouselook', 'cl_observercrosshair', 'cl_overdraw_test', 'cl_panelanimation', 'cl_particleeffect_aabb_buffer', 'cl_pclass', 'cl_pdump', 'cl_phys_props_enable', 'cl_phys_props_max', 'cl_phys_timescale', 'cl_pitchdown', 'cl_pitchspeed', 'cl_pitchup', 'cl_precacheinfo', 'cl_pred_optimize', 'cl_predict', 'cl_predictionlist', 'cl_predictweapons', 'cl_radaralpha', 'cl_radartype', 'cl_ragdoll_collide', 'cl_ragdoll_physics_enable', 'cl_rebuy', 'cl_removedecals', 'cl_resend', 'cl_righthand', 'cl_scalecrosshair', 'cl_SetupAllBones', 'cl_show_splashes', 'cl_showanimstate', 'cl_showanimstate_log', 'cl_showents', 'cl_showerror', 'cl_showevents', 'cl_showfps', 'cl_showpluginmessages', 'cl_showpos', 'cl_ShowSunVectors', 'cl_showtextmsg', 'cl_sidespeed', 'cl_slist', 'cl_smooth', 'cl_smoothtime', 'cl_soundemitter_flush', 'cl_soundfile', 'cl_soundscape_flush', 'cl_soundscape_printdebuginfo', 'cl_spec_mode', 'cl_sun_decay_rate', 'cl_team', 'cl_timeout', 'cl_updaterate', 'cl_upspeed', 'cl_view', 'cl_winddir', 'cl_windspeed', 'cl_wpn_sway_interp', 'cl_wpn_sway_scale', 'cl_yawspeed', 'clear', 'clear_debug_overlays', 'clientport', 'closecaption', 'cmd', 'collision_shake_amp', 'collision_shake_freq', 'collision_shake_time', 'colorcorrectionui', 'commentary_firstrun', 'commentary_testfirstrun', 'con_drawnotify', 'con_enable', 'con_notifytime', 'con_nprint_bgalpha', 'con_nprint_bgborder', 'con_trace', 'condump', 'connect', 'contimes', 'coop', 'CreateHairball', 'CreatePredictionError', 'creditsdone', 'crosshair', 'cs_disko', 'cs_ShowStateTransitions', 'cs_stacking_num_levels', 'cvarlist', 'deathmatch', 'debug_physimpact', 'decalfrequency', 'default_fov', 'demo_debug', 'demo_fastforwardfinalspeed', 'demo_fastforwardramptime', 'demo_fastforwardstartspeed', 'demo_gototick', 'demo_interpolateview', 'demo_pause', 'demo_pauseatservertick', 'demo_quitafterplayback', 'demo_recordcommands', 'demo_resume', 'demo_timescale', 'demo_togglepause', 'demolist', 'demos', 'demoui', 'developer', 'devshots_nextmap', 'devshots_screenshot', 'differences', 'disconnect', 'disp_dynamic', 'disp_modlimit', 'disp_modlimit_down', 'disp_modlimit_up', 'disp_numiterations', 'dispcoll_drawplane', 'displaysoundlist', 'drawcross', 'drawline', 'drawradar', 'dsp_automatic', 'dsp_db_min', 'dsp_db_mixdrop', 'dsp_dist_max', 'dsp_dist_min', 'dsp_enhance_stereo', 'dsp_facingaway', 'dsp_mix_max', 'dsp_mix_min', 'dsp_off', 'dsp_player', 'dsp_reload', 'dsp_room', 'dsp_slow_cpu', 'dsp_spatal', 'dsp_speaker', 'dsp_vol_2ch', 'dsp_vol_4ch', 'dsp_vol_5ch', 'dsp_volume', 'dsp_water', 'dt_flush', 'dtwarning', 'dtwatchent', 'dtwatchvar', 'dump_globals', 'dump_panels', 'dumpstringtables', 'echo', 'editdemo', 'editor_toggle', 'endmovie', 'endround', 'english', 'ent_bbox', 'ent_debugkeys', 'ent_dump', 'ent_fire', 'ent_info', 'ent_messages', 'ent_mesages_draw', 'ent_name', 'ent_pause', 'ent_pivot', 'ent_rbox', 'ent_remove', 'ent_remove_all', 'ent_setname', 'ent_show_response_criteria', 'ent_step', 'ent_text', 'envmap', 'escape', 'exec', 'exit', 'fadein', 'fadeou', 'filesystem_buffer_size', 'find', 'fire_absorbrate', 'fire_dmgbase', 'fire_dmginterval', 'fire_dmgscale', 'fire_extabsorb', 'fire_extscale', 'fire_growthrate', 'fire_heatscale', 'fire_icomingheatscale', 'fire_maxabsorb', 'firetarget', 'firstperson', 'fish_debug', 'fish_dormant', 'flex_expression', 'flex_looktime', 'flex_maxawaytime', 'flex_maxplayertime', 'flex_minawaytime', 'flex_minplayertime', 'flex_ruls', 'flex_smooth', 'flex_talk', 'flush', 'flush_unlocked', 'fo_color', 'fog_colorskybox', 'fog_enable', 'fog_enable_water_fog', 'fog_enableskybox', 'fog_end', 'fog_endskybox', 'fog_override', 'fog_start', 'fog_startskybox', 'force_centerview', 'fov', 'fps_max', 'free_pass_peek_debug', 'fs_printopenfiles', 'fs_warning_level', 'func_break_max_pieces', 'func_breakdmg_bullet', 'func_breakdmg_club', 'func_breakdmg_eplosive', 'g_debug_doors', 'g_debug_ragdoll_removal', 'g_debug_ragdoll_visualize', 'g_debug_trackpather', 'g_debug_transitions', 'g_debug_vehiclebase', 'g_debug_vehicledriver', 'g_debug_vehicleexit', 'g_debug_vehiclesound', 'g_jeepexitspeed', 'g_Language', 'g_ragdoll_fadespeed', 'g_ragdoll_lvfadespeed', 'g_ragdoll_maxcount', 'gameui_activate', 'gameui_allowescape', 'gameui_hide', 'gameui_preventescape', 'getpos', 'give', 'gl_clear', 'god', 'groudlist', 'heartbeat', 'help', 'hideconsole', 'hidehud', 'hidepanel', 'hideradar', 'host_framerate', 'host_limitlocal', 'host_map', 'host_profile', 'host_runofftime', 'host_showcachemiss', 'host_sleep', 'host_speeds', 'host_timescale', 'host_writeconfig', 'hostage_debug', 'hostname', 'hostport', 'hud_autoreloadscript', 'hud_centerid', 'hud_deathnotice_time', 'hud_drawhistory_time', 'hud_fastswitch', 'hud_jeephint_numentries', 'hud_reloadscheme', 'hud_saytext_time', 'hud_showtargetid', 'hurtme', 'impulse', 'incrementvar', 'invnext', 'invprev', 'ip', 'joy_advanced', 'joy_advaxisr', 'joy_advaxisu', 'joy_advaxisv', 'joy_advaxisx', 'joy_advaxisy', 'joy_advaxisz', 'joy_diagonalpov', 'joy_forwardsensitivity', 'joy_forwardthreshold', 'joy_name', 'joypitchsensitivity', 'joy_pitchthreshold', 'joy_sidesensitivity', 'joy_sidethreshold', 'joy_wingmanwarrier_centerhack', 'joy_wingmanwarrier_turnhack', 'joy_yawsensitivity', 'joy_yawthreshold', 'joyadvancedupdate', 'joystick', 'jpeg', 'jpeg_quality', 'kdtree_test', 'key_findbinding', 'key_listboundkeys', 'key_updatelayout', 'kick', 'kickid', 'kill', 'killserver', 'lastinv', 'light_crosshair', 'linefile', 'list', 'listdemo', 'listid', 'listip', 'listmodels', 'load', 'lod_Enable', 'lod_TransitionDist', 'log', 'logaddress_add', 'logaddress_del', 'logaddress_delall', 'logaddress_list', 'lookspring', 'lookstrafe', 'lservercfgfile', 'm_cusomaccel', 'm_customaccel_exponent', 'm_customaccel_max', 'm_customaccel_scale', 'm_filter', 'm_forward', 'm_mouseaccel1', 'm_mouseaccel2', 'm_mousespeed', 'm_pitch', 'm_side', 'm_yaw', 'map', 'map_background', 'map_commentary', 'map_edit', 'map_noareas', 'map_setbombradius', 'map_showbombradius', 'map_showspawnpoints', 'mapcyclefile', 'maps', 'mat_antialias', 'mat_bloom', 'mat_bufferprimitives', 'mat_bumpbasis', 'mat_bumpmap', 'mat_camerarendertargetoverlaysize', 'mat_clipz', 'mat_compressedtextures', 'mat_configcurrent', 'mat_crosshair', 'mat_debug', 'mat_debugalttab', 'mat_debugdepth', 'mat_debugdepthmode', 'mat_debugdepthval', 'mat_debugdepthvalmax', 'mat_depthbias_decal', 'mat_depthbias_normal', 'mat_diffuse', 'mat_drawflat', 'mat_drawwater', 'mat_dxlevel', 'mat_dynamic_tonemapping', 'mat_edit', 'mat_envmapsize', 'mat_envmaptgasize', 'mat_fastnobump', 'mat_fastpecular', 'mat_fillrate', 'mat_filterlightmaps', 'mat_filtertextures', 'mat_force_tonemap_scale', 'mat_forceaniso', 'mat_forcedynamic', 'mat_forcehardwaresync', 'mat_forcemanagedtextureintohardware', 'mat_frame_sync_enable', 'mat_frame_sync_force_texture', 'mat_framebuffercopyoverlaysize', 'mat_fullbright', 'mat_hdr_enabled', 'mat_hdr_level', 'mat_hdr_manual_tonemap_rate', 'mat_hdr_tonemapscale', 'mat_hdroverbrightrange', 'mat_hsv', 'mat_info', 'mat_leafvis', 'mat_levelflush', 'mat_loadtextures', 'mat_luxels', 'mat_maxframelatency', 'mat_measurefillrate', 'mat_mipmaptextures', 'mat_monitorgamma', 'mat_norendering', 'mat_normalmaps', 'mat_normals', 'mat_parallaxmap', 'mat_picmip', 'mat_proxy', 'mat_reducefillrate', 'mat_reloadallmaterials', 'mat_reloadmaterial', 'mat_reloadtextures', 'mat_reversedepth', 'mat_savechanges', 'mat_setvideomode', 'mat_shadowstate', 'mat_show_ab_hdr', 'mat_show_texture_memory_usage', 'mat_showcamerarendertarget', 'mat_showenvmapmask', 'mat_showframebuffertexture', 'mat_showlightmapcomponent', 'mat_showlightmappage', 'mat_showlowresimage', 'mat_showmaterials', 'mat_showmaterialsverbose', 'mat_showmiplevels', 'mat_showtextures', 'mat_showwatertextures', 'mat_slopescaledepthbias_decal', 'mat_slopescaledepthbias_normal', 'mat_softwarelighting', 'mat_softwareskin', 'mat_specular', 'mat_spewvertexandpixelshaders', 'mat_stub', 'mat_suppress', 'mat_surfaceid', 'mat_surfacemat', 'mat_texture_liit', 'mat_texture_list', 'mat_texture_list_all', 'mat_texturelist_directories', 'mat_texturelist_files', 'mat_trilinear', 'mat_vsync', 'mat_wateroverlaysize', 'mat_wireframe', 'mat_yuv', 'maxplayers', 'mem_dumpstats', 'mem_force_flush', 'memory', 'menuselect', 'minisave', 'mod_forcedata', 'mod_load_async', 'mod_test_mesh_not_available', 'mod_test_not_available', 'mod_test_verts_not_available', 'mod_trace_load', 'motdfile', 'mp_allowNPCs', 'mp_allowspectators', 'mp_autocrosshair', 'mp_autokick', 'mp_autoteambalance', 'mp_buytime', 'mp_c4timer', 'mp_chattime', 'mp_decals', 'mp_defaultteam', 'mp_facefronttime', 'mp_fadetoblack', 'mp_falldamage', 'mp_feetyawrate', 'mp_flashlight', 'mp_footsteps', 'mp_forcecamera', 'mp_forcerespawn', 'mp_fraglimit', 'mp_freezetime', 'mp_friendlyfire', 'mp_hostagepenalty', 'mp_humantea', 'mp_ik', 'mp_limitteams', 'mp_logdetail', 'mp_maxrounds', 'mp_playerid', 'mp_playerid_delay', 'mp_playerid_hold', 'mp_restartgame', 'mp_roundtime', 'mp_spawnprotectiontime', 'mp_startmoney', 'mp_teamlist', 'mp_teamoverride', 'mp_teamplay', 'mp_timelimit', 'mp_tkpunish', 'm_weaponstay', 'mp_winlimit', 'muzzleflash_light', 'name', 'nav_analyze', 'nav_area_bgcolor', 'nav_avoid', 'nav_begin_area', 'nav_build_ladder', 'nav_check_file_consistency', 'nav_check_floor', 'nav_clear_walkable_marks', 'nav_compress_id', 'nav_connect', 'nav_coplanar_slope_limit', 'nav_corner_lower', 'nav_corner_place_on_ground', 'nav_corner_raise', 'nav_corner_select', 'nav_create_place_on_ground', 'nav_crouch', 'nav_delete', 'nav_disconnect', 'nav_dont_hide', 'nav_edit', 'nav_end_area', 'nav_generate', 'nav_generate_incremental', 'nav_jump', 'nav_ladder_flip', 'nav_load', 'nav_make_sniper_spots', 'nav_mark', 'nav_mark_unnamed', 'nav_mark_walkable', 'nav_merge', 'nav_no_hostages', 'nav_no_jump', 'nav_place_floodfill', 'nav_place_list', 'nav_place_pick', 'nav_place_replace', 'nav_precise', 'nav_quicksave', 'nav_remove_unused_jump_areas', 'nav_restart_after_analysis', 'nav_run', 'nav_save', 'nav_set_place_mode', 'nav_show_approach_points', 'nav_show_area_info', 'nav_show_danger', 'nav_show_ladder_bounds', 'nav_show_player_counts', 'nav_slope_limit', 'nav_snap_to_grid', 'nav_splice', 'nav_split', 'nav_split_place_on_ground', 'nav_stand', 'nav_stop', 'nav_strip', 'nav_toggle_place_mode', 'nav_toggle_place_painting', 'nav_transient', 'nav_unmark', 'nav_update_blocked', 'nav_use_place', 'nav_walk', 'nav_warp_to_mark', 'net_blockmsg', 'net_channels', 'net_chokeloop', 'net_drawslider', 'net_droppackets', 'net_fakelag', 'net_fakeloss', 'net_graph', 'net_graphheight', 'net_graphos', 'net_graphsolid', 'net_maxfilesize', 'net_maxfragments', 'net_scale', 'net_showdrop', 'net_showevents', 'net_showfragments', 'net_showmsg', 'net_showpeaks', 'net_showsplits', 'net_showtcp', 'net_showudp', 'net_start', 'next', 'nextdemo', 'noclip', 'notarget', 'npc_ammo_deplete', 'npc_bipass', 'npc_combat', 'npc_conditions', 'npc_create', 'npc_create_aimed', 'npc_create_equipment', 'npc_detroy', 'npc_destroy_unselected', 'npc_enemies', 'npc_focus', 'npc_freeze', 'npc_go', 'npc_go_do_run', 'npc_go_random', 'npc_heal', 'npc_height_adjust', 'npc_kill', 'npc_nearest', 'npc_reset', 'npc_route', 'npc_select', 'npc_sentences', 'npc_speakall', 'npc_squads', 'npc_steering', 'npc_steering_all', 'npc_task_text', 'npc_tasks', 'npc_thinknow', 'npc_viewcone', 'npc_vphysics', 'old_radiusdamage', 'overview_alpha', 'overview_health', 'overview_locked', 'overview_mode', 'overview_names', 'overview_tracks', 'overview_zoom', 'particle_simulateoverflow', 'password', 'path', 'pause', 'perfui', 'perfvisualenchmark', 'perfvisualbenchmark_abort', 'phonemedelay', 'phonemefilter', 'phonemesnap', 'phys_impactforcescale', 'phys_penetration_error_time', 'phys_pushscale', 'phys_speeds', 'phys_stressbodyweights', 'phys_swap', 'phys_timescale', 'phys_upimpactforcescale', 'physics_budget', 'physics_debug_entity', 'physics_highlight_active                  cmd', 'physics_report_active', 'physics_select', 'physicsshadowupdate_render', 'picker', 'ping', 'pixelvis_debug', 'play', 'playdemo', 'player_old_armor', 'payflush', 'playgamesound', 'playsoundscape', 'playvol', 'plugin_load', 'plugin_pause', 'plugin_pause_all', 'plugin_print', 'plugin_unload', 'plugin_unpause', 'plugin_unpause_all', 'progress_enable', 'prop_crosshair', 'prop_debug', 'props_break_max_pieces', 'pwatchent', 'pwatchvar', 'quit', 'quti', 'r_3dnow', 'r_3dsky', 'r_AirboatViewDampenDamp', 'r_AirboatViewDampenFreq', 'r_AirboatViewZHeight', 'r_ambientlightingonly', 'r_aspectratio', 'r_avglight', 'r_avglightmap', 'r_cheapwaterend', 'r_cheapwaterstart', 'r_cleardecals', 'r_ClipAreaPortals', 'r_colorstaticprops', 'r_debugcheapwater', 'r_debugrandomstaticlighting', 'r_decal_cullsize', 'r_decals', 'r_decalstaticprops', 'r_DispBuildabe', 'r_DispDrawAxes', 'r_DispWalkable', 'r_DoCovertTransitions', 'r_dopixelvisibility', 'r_drawbatchdecals', 'r_DrawBeams', 'r_drawbrushmodels', 'r_drawclipbrushes', 'r_drawdecals', 'r_drawdetailprops', 'r_DrawDisp', 'r_drawentities', 'r_drawflecks', 'r_drawfullskybox', 'r_drawleaf', 'r_drawlightcache', 'r_drawlightinfo', 'r_drawlights', 'r_drawmodeldecals', 'r_DrawModelLightOrigin', 'r_drawmodelstatsoverlay', 'r_drawmodelstatsoverlaydistance', 'r_drawmodelstatsoverlaymax', 'r_drawmodeltatsoverlaymin', 'r_drawopaquerenderables', 'r_drawopaqueworld', 'r_drawothermodels', 'r_drawparticles', 'r_drawpixelvsibility', 'r_DrawPortals', 'r_DrawRain', 'r_drawrenderboxes', 'r_drawropes', 'r_drawskybox', 'r_DrawSpecificStaticProp', 'r_drawsprites', 'r_drawstaticprops', 'r_drawtranslucentrenderables', 'r_drawtranslucentworld', 'r_drawvgui', 'r_drawviewmodel', 'r_drawworld', 'r_dscale_basefov', 'r_dscale_fardist', 'r_dscale_farscale', 'r_dscale_neardist', 'r_dscale_nearscale', 'r_dynamic', 'r_eyeglintlodpixels', 'r_eyegloss', 'r_eyemove', 'r_eyes', 'r_eyeshift_x', 'r_eyeshift_y', 'r_eyeshift_z', 'r_eyesize', 'r_eyewaterepsilon', 'r_farz', 'r_fastzreject', 'r_flashlightconstant', 'r_flashlightdrawfrustum', 'r_flashlightdrawfrustumbbox', 'r_flashlightdrawsweptbbox', 'r_flashlightfar', '_flashlightfov', 'r_flashlightlinear', 'r_flashlightlockposition', 'r_flashlightmodels', 'r_flashlightnear', 'r_flashlightnodraw', 'r_flashlightoffsetx', 'r_flashlightoffsety', 'r_flashlightoffsetz', 'r_flashlightquadratic', 'r_flashlightvisualizetrace', 'r_flex', 'r_flushlod', 'r_ForceRestore', 'r_ForceWaterLeaf', 'r_frustumcullworld', 'r_JeepFOV', 'r_JeepViewBlendTo', 'r_JeepViewBlendToScale', 'r_JeepViewBlendoTime', 'r_JeepViewDampenDamp', 'r_JeepViewDampenFreq', 'r_JeepViewZHeight', 'r_lightaverage', 'r_lightcache_numambientsamples', 'r_lightcachecenter', 'r_lightinterp', 'r_lightmap', 'r_lightstyle', 'r_lockpvs', 'r_lod', 'r_lod_noupdate', 'r_mapextents', 'r_maxdlights', 'r_maxmodeldecal', 'r_maxnewsample', 'r_maxsampledist', 'r_minnewsamples', 'r_mmx', 'r_modellodscale', 'r_modelwireframedecal', 'r_ewflashlight', 'r_newproplighting', 'r_nohw', 'r_norefresh', 'r_nosw', 'r_novis', 'r_occludeemaxarea', 'r_occluderminarea', 'r_occludermincount', 'r_occlusion', 'r_occlusionspew', 'r_overlayfadeenable', 'r_overlayfademax', 'r_overlayfademin', 'r_overlaywireframe', 'r_PhysPropStaticLighting', 'r_pixelvis_partial', 'r_portalscloseall', 'r_portalsopenall', 'r_PortalTestEnts', 'r_printdecalinfo', 'r_propsmaxdist', 'r_radiosity', 'r_rainalpha', 'r_rainalphapow', 'r_raindensity', 'r_RaiHack', 'r_rainlength', 'r_RainProfile', 'r_RainRadius', 'r_RainSideVel', 'r_RainSimulate', 'r_rainspeed', 'r_RainSplashPercentage', 'r_rainwidth', 'r_renderoverlayfragment', 'r_rootlod', 'r_ropebatch', 'r_ropetranslucent', 'r_screenfademaxsize', 'r_screenfademinsize', 'r_screenoverlay', 'r_sequence_debug', 'r_shadowangles', 'r_shadowblobbycutoff', 'r_shadowcolor', 'r_shadowdir', 'r_shadowdist', 'r_shadowids', 'r_shadowmaxrendered', 'r_shadowrendertotexture', 'r_hadows', 'r_shadowwireframe', 'r_showenvcubemap', 'r_ShowViewerArea', 'r_skin', 'r_skybox', 'r_snapportal', 'r_spray_lifetime', 'r_sse', 'r_sse2', 'r_staticpropinfo', 'r_teeth', 'r_TransitionSensitivity', 'r_updaterefracttexture', 'r_vehicleBrakeRate', 'r_vehicleDrawDebug', 'r_VehicleViewClamp', 'r_VehicleViewDampen', 'r_visocclusion', 'r_visualizelighttraces', 'r_visualizelighttracesshowfulltrace', 'r_visualizeproplightcaching', 'r_visualizetraces', 'r_WaterDrawReflection', 'r_WaterrawRefraction', 'r_waterforceexpensive', 'r_waterforcereflectentities', 'r_worldlightmin', 'r_worldlights', 'radio1', 'radio2', 'radio3', 'rate', 'rcon', 'rcon_address', 'rcon_password', 'rebuy', 'recompute_speed', 'record', 'reload', 'removeid', 'removeip', 'replaydelay', 'report_entities', 'report_simthinklist', 'report_soundpatch', 'report_soundpatch', 'report_touchlinks', 'restart', 'retry', 'revert', 'room_type', 'rope_averagelight', 'rope_ollide', 'rope_drawlines', 'rope_shake', 'rope_smooth', 'rope_smooth_enlarge', 'rope_smooth_maxalpha', 'rope_smooth_maxalphawidth', 'rope_smooth_minalpha', 'rope_smooth_minwidth', 'rope_subdiv', 'rope_wind_dist', 'save', 'say', 'say_team', 'scene_allowoverrides', 'scene_flatturn', 'scene_flush', 'scene_forcecombined', 'scene_maxcaptionradius', 'scene_print', 'scene_showfaceto', 'scene_showlook', 'scene_showmoveto', 'scr_centertime', 'screenshot', 'sensitivity', 'servercfgfile', 'setang', 'setinfo', 'setmaster', 'setmodel', 'setpause', 'setpos', 'shake', 'shake_show', 'shake_stop', 'showbudget_texture', 'showconsole', 'showhitlocation', 'showinfo',
    ]

    # Python braces
    braces = [
        #'space', 'tab', 'enter', 'return', 'escape', 'esc', 'backspace', 'delete', 'insert', 'home', 'end', 'pgup', 'pgdn', 'up', 'down', 'left', 'right', 'scrolllock', 'capslock', 'numlock', 'numpad0', 'numpadins', 'numpad1', 'numpadend', 'numpad2', 'numpaddown', 'numpad3', 'numpadpgdn', 'numpad4', 'numpadleft', 'numpad5', 'numpadclear', 'numpad6', 'numpadright', 'numpad7', 'numpadhome', 'numpad8', 'numpadup', 'numpad9', 'numpadpgup', 'control', 'alt', 'shift', 'tab', 'enter', 'escape', 'space', 'backspace', 'uparrow', 'downarrow', 'leftarrow', 'rightarrow', 'alt', 'ctrl', 'shift', 'ins', 'del', 'pgdn', 'pgup', 'home', 'end', 'kp_home', 'kp_uparrow', 'kp_pgup', 'kp_leftarrow', 'kp_5', 'kp_rightarrow', 'kp_end', 'kp_downarrow', 'kp_pgdn', 'kp_enter', 'kp_ins', 'kp_del', 'kp_slash', 'kp_multiply', 'kp_minus', 'kp_plus', 'capslock', 'mwheeldown', 'mwheelup', 'mouse1', 'mouse2', 'mouse3', 'mouse4', 'mouse5', 'pause', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
        'SPACE', 'TAB', 'ENTER', 'RETURN', 'ESCAPE', 'BACKSPACE', 'DELETE', 'INSERT', 'HOME', 'END', 'PGUP', 'PGDN', 'UP', 'DOWN', 'LEFT', 'RIGHT', 'SCROLLLOCK', 'CAPSLOCK', 'NUMLOCK', 'NUMPAD0', 'NUMPADINS', 'NUMPAD1', 'NUMPADEND', 'NUMPAD2', 'NUMPADDOWN', 'NUMPAD3', 'NUMPADPGDN', 'NUMPAD4', 'NUMPADLEFT', 'NUMPAD5', 'NUMPADCLEAR', 'NUMPAD6', 'NUMPADRIGHT', 'NUMPAD7', 'NUMPADHOME', 'NUMPAD8', 'NUMPADUP', 'NUMPAD9', 'NUMPADPGUP', 'CONTROL', 'ALT', 'SHIFT', 'TAB', 'ENTER', 'ESCAPE', 'SPACE', 'BACKSPACE', 'UPARROW', 'DOWNARROW', 'LEFTARROW', 'RIGHTARROW', 'ALT', 'CTRL', 'SHIFT', 'PGDN', 'PGUP', 'HOME', 'END', 'KP_HOME', 'KP_UPARROW', 'KP_PGUP', 'KP_LEFTARROW', 'KP_5', 'KP_RIGHTARROW', 'KP_END', 'KP_DOWNARROW', 'KP_PGDN', 'KP_ENTER', 'KP_INS', 'KP_DEL', 'KP_SLASH', 'KP_MULTIPLY', 'KP_MINUS', 'KP_PLUS', 'CAPSLOCK', 'MWHEELDOWN', 'MWHEELUP', 'MOUSE1', 'MOUSE2', 'MOUSE3', 'MOUSE4', 'MOUSE5', 'PAUSE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
    ]
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward
        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])

        rules = []

        # Keyword, operator, and brace rules
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
            for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
            for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
            for b in PythonHighlighter.braces]

        # All other rules
        rules += [
            # 'self'
            (r'\bself\b', 0, STYLES['self']),

            # Double-quoted string, possibly containing escape sequences
            #(r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            #(r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            # 'def' followed by an identifier
            (r'\bbind\b\s*(\w+)', 1, STYLES['defclass']),
            # 'class' followed by an identifier
            (r'\balias\b\s*(\w+)', 1, STYLES['defclass']),

            # From '//' until a newline
            (r'//[^\n]*', 0, STYLES['comment']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]


    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = expression.cap(nth).length()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)


    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = text.length() - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False
        
        