VERSION 5.00
Begin VB.Form MainForm 
   Caption         =   "Form1"
   ClientHeight    =   4960
   ClientLeft      =   120
   ClientTop       =   470
   ClientWidth     =   8780
   LinkTopic       =   "Form1"
   ScaleHeight     =   4960
   ScaleWidth      =   8780
   Begin VB.CommandButton mainBtn_sel_file 
      Caption         =   "绑定目录"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   120
      TabIndex        =   3
      Top             =   4200
      Width           =   8410
   End
   Begin VB.Frame Frame1 
      Caption         =   "当前目录绑定目录"
      Height          =   975
      Left            =   120
      TabIndex        =   1
      Top             =   3120
      Width           =   8410
      Begin VB.TextBox Text1 
         Height          =   615
         Left            =   120
         TabIndex        =   2
         Top             =   240
         Width           =   8170
      End
   End
   Begin VB.CommandButton mainBtn_copy 
      Caption         =   "一键【点击】复制下载脚本"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2895
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   8535
   End
End
Attribute VB_Name = "MainForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
