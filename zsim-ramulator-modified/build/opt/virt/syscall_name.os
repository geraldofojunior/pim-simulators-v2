ELF          >                    �8          @     @   H�    ��  wH�    ��H���INVALID io_setup io_destroy io_submit io_cancel io_getevents setxattr lsetxattr fsetxattr getxattr lgetxattr fgetxattr listxattr llistxattr flistxattr removexattr lremovexattr fremovexattr getcwd lookup_dcookie eventfd2 epoll_create1 epoll_ctl epoll_pwait dup dup3 inotify_init1 inotify_add_watch inotify_rm_watch ioctl ioprio_set ioprio_get flock mknodat mkdirat unlinkat symlinkat linkat renameat umount2 mount pivot_root nfsservctl fallocate faccessat chdir fchdir chroot fchmod fchmodat fchownat fchown openat close vhangup pipe2 quotactl getdents64 read write readv writev pread64 pwrite64 preadv pwritev pselect6 ppoll signalfd4 vmsplice splice tee readlinkat sync fsync fdatasync sync_file_range timerfd_create timerfd_settime timerfd_gettime utimensat acct capget capset personality exit exit_group waitid set_tid_address unshare futex set_robust_list get_robust_list nanosleep getitimer setitimer kexec_load init_module delete_module timer_create timer_gettime timer_getoverrun timer_settime timer_delete clock_settime clock_gettime clock_getres clock_nanosleep syslog ptrace sched_setparam sched_setscheduler sched_getscheduler sched_getparam sched_setaffinity sched_getaffinity sched_yield sched_get_priority_max sched_get_priority_min sched_rr_get_interval restart_syscall kill tkill tgkill sigaltstack rt_sigsuspend rt_sigaction rt_sigprocmask rt_sigpending rt_sigtimedwait rt_sigqueueinfo rt_sigreturn setpriority getpriority reboot setregid setgid setreuid setuid setresuid getresuid setresgid getresgid setfsuid setfsgid times setpgid getpgid getsid setsid getgroups setgroups uname sethostname setdomainname getrlimit setrlimit getrusage umask prctl getcpu gettimeofday settimeofday adjtimex getpid getppid getuid geteuid getgid getegid gettid sysinfo mq_open mq_unlink mq_timedsend mq_timedreceive mq_notify mq_getsetattr msgget msgctl msgrcv msgsnd semget semctl semtimedop semop shmget shmctl shmat shmdt socket socketpair bind listen accept connect getsockname getpeername sendto recvfrom setsockopt getsockopt shutdown sendmsg recvmsg readahead brk munmap mremap add_key request_key keyctl clone execve swapon swapoff mprotect msync mlock munlock mlockall munlockall mincore madvise remap_file_pages mbind get_mempolicy set_mempolicy migrate_pages move_pages rt_tgsigqueueinfo perf_event_open accept4 recvmmsg arch_specific_syscall wait4 prlimit64 fanotify_init fanotify_mark name_to_handle_at open_by_handle_at clock_adjtime syncfs setns sendmmsg process_vm_readv process_vm_writev kcmp finit_module sched_setattr sched_getattr renameat2 seccomp getrandom memfd_create bpf execveat userfaultfd membarrier mlock2 syscalls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                �                                               int                 3b               >    �                  ��       >W        �       �   	�   �   
�            �   	        �    %  $ >  $ >   :;I  .?:;nI@�B   :;I   I  & I  	I  
! I/  4 :;I                   U               �U�                ,                                            v    O   �      build/opt/virt /usr/include  syscall_name.cpp   stdint.h     	        � � � unsigned int syscallNames /home/geraldo/Tools/zsim-ramulator build/opt/virt/syscall_name.cpp syscall GNU C++11 5.4.1 20160904 -march=core2 -g -g -O3 -std=c++11 -funroll-loops -fomit-frame-pointer -fno-stack-protector -fPIC -fabi-version=2 unsigned char char uint32_t long int long unsigned int short unsigned int signed char GetSyscallName _Z14GetSyscallNamej short int sizetype  GCC: (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 20160904        zR x�                                                   ��                                                                                                                                           �                                 	                                                                                                                                                                           $                                            )                     syscall_name.cpp _ZL12syscallNames .LC0 _Z14GetSyscallNamej                 ��������             ��������                                                                          &                     0       (             =       0             F       8             P       @             Z       H             c       P             m       X             w       `             �       h             �       p             �       x             �       �             �       �             �       �             �       �             �       �             �       �             �       �             �       �                    �                   �                     �             	      �                   �             )      �             :      �             @      �             K                   V                  \                  d                  l                   u      (                  0            �      8            �      @            �      H            �      P            �      X                    `                    h                    p                    x            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �                  �                  �                  �                  �                  �                    �            *                   /                  5                  ;                  B                   J      (            S      0            Z      8                    @            b      H            k      P            q      X            {      `            �      h            �      p            �      x                    �                    �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �                  �                  �                  �                  �            '                   .                  >                  F                  L                   \      (            l      0            v      8            �      @            �      H            �      P            �      X            �      `            �      h            �      p            �      x            �      �            �      �                  �                  �                  �            /      �            6      �            =      �            L      �            _      �            r      �            �      �            �      �            �      �            �      �            �      �            �                   �                                    
                                           (            #      0            1      8            >      @            M      H            [      P            k      X            {      `            �      h            �      p            �      x            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �                  �                  �                  �                  �                  �            %      �            /                   9                  ?                  K                  Y                   c      (            m      0            w      8            }      @            �      H            �      P            �      X            �      `            �      h            �      p            �      x            �      �            �      �            �      �            �      �            �      �            �      �            �      �            �      �                  �                  �            "      �            0      �            7      �            >      �            E      �            L      �            S                   Z                  e                  k                  r                   y      (                  0            �      8            �      @            �      H            �      P            �      X            �      `            �      h            �      p            �      x            �      �            �      �            �      �            �      �            �      �                  �            	      �                  �                  �                  �            %      �            -      �            9      �            @      �            F      �                    �                                 M                  T                  \                  e                   k      (            q      0            y      8            �      @            �      H            �      P            �      X            �      `            �      h            �      p            �      x            �      �            �      �            �      �            	      �            	      �            	      �                    �                    �                    �                    �                    �                    �                    �                    �                    �                    �                                                                                                                  2	      (            8	      0            B	      8            P	      @            ^	      H            p	      P            �	      X            �	      `            �	      h            �	      p            �	      x            �	      �            �	      �            �	      �            �	      �            �	      �            �	      �            
      �            	
      �            
      �             
      �            $
      �            -
      �            9
      �            D
      �            K
             
   
                  
      e              
      =              
                                  )       
              0       
      9      7       
      h      E       
            L       
      �       S       
      &      X       
            e       
              l       
            q       
      E      x       
      T      �                     �       
      ]       �       
              �       
      �       �       
      r      �       
             �                            
   	                                \                                            .symtab .strtab .shstrtab .rela.text .data .bss .rodata.str1.1 .text.unlikely .rela.data.rel.ro.local .rela.debug_info .debug_abbrev .debug_loc .rela.debug_aranges .rela.debug_line .debug_str .comment .note.GNU-stack .rela.eh_frame                                                                                              @                                           @                     0                           &                     ]                                      ,                     ]                                      1      2               ]       T
                            @                     �
                                     T                     �
      �                              O      @               @      �                          l                      �      �                              g      @               5      (         	                 x                      �      �                              �                      /      9                              �                      h      0                              �      @               87      0                           �                      �      z                              �      @               h7                                 �      0                     {                            �      0               �      3                             �                      �                                     �                     �      0                              �      @               �7                                                       �7      �                                                    �      �                          	                      �      =                              