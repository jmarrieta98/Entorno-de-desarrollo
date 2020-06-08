Public Class Form1
    REM Declaración de variables
    Const Pi As Single = 3.141592654
    Dim R, A, V As Single

    REM Contenido del formulario
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
Me.Text = "Cálculo volumen cilindro"
ButtonCalcular.Text = "Calcular Volumen"
Label1.Text = "Introduzca aquí el diámetro, en metros"
Label2.Text = "Introduzca aquí la altura, en metros"
    End Sub

    REM Cálculo y muestra resultados
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ButtonCalcular.Click
        R = Val(TextBox1.Text)/2
        A = Val(TextBox2.Text)
        V = Pi*(R^2) *A
        LabelResultados.Font = New Font("Arial", 10, FontStyle.Bold)
        LabelResultados.TextAlign = ContentAlignment.MiddleCenter
        LabelResultados.Text = "El volumen del cilindro es de " & V & " metros cúbicos"
    End Sub
End Class
