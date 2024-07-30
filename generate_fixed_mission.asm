; ------------------------------------------------------------------------------
; Generate Fixed Mission
; Attempts to generate a mission from a Wonder Mail S code!
;
; Returns: 1 if successful, 0 if not!
; ------------------------------------------------------------------------------

.relativeinclude on
.nds
.arm

.definelabel MaxSize, 0x810

; Uncomment/comment the following labels depending on your version.

; For US
;.include "lib/stdlib_us.asm"
;.definelabel ProcStartAddress, 0x022E7248
;.definelabel ProcJumpAddress, 0x022E7AC0
;.definelabel DecryptWonderMailString, 0x0204DD80
;.definelabel IsMissionSuspendedAndValid, 0x0205C854
;.definelabel AlreadyHaveMission, 0x0205EC98
;.definelabel AddMissionToJobList, 0x0205F0B8

; For EU
.include "lib/stdlib_eu.asm"
.definelabel ProcStartAddress, 0x022E7B88
.definelabel ProcJumpAddress, 0x022E8400
.definelabel WonderMailStringToMission, 0x0204E0B8
.definelabel IsMissionSuspendedAndValid, 0x0205CBD0
.definelabel AlreadyHaveMission, 0x0205F100
.definelabel AddMissionToJobList, 0x0205F434

; File creation
.create "./code_out.bin", 0x022E7B88
	.org ProcStartAddress
	.area MaxSize
		
		push r10
		sub r13,r13,#0x24
		mov r10,#0
		ldr r0,=WONDER_MAIL_S_CODE
		mov r1,r13
		bl WonderMailStringToMission
		cmp r0,#0
		beq @@ret
		mov r0,r13
		bl IsMissionSuspendedAndValid
		cmp r0,#0
		beq @@ret
		mov r0,r13
		bl AlreadyHaveMission
		cmp r0,#0
		bne @@ret
		mov r0,r13
		bl AddMissionToJobList
		mov r10,#1
	@@ret:
		mov r0,r10
		add r13,r13,#0x24
		pop r10
		b ProcJumpAddress
		.pool
	WONDER_MAIL_S_CODE:
		.asciiz "9NX-6WQ&T77@Y9H516S87PWW58#@MFF&47" ; Add your own code here!
	.endarea
.close
