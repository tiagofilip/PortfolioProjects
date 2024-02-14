import tkinter as tk # Importação da biblioteca tkinter
import pandas as pd # Importação da biblioteca pandas
from tkinter import messagebox, filedialog # Importação do módulo da messagebox e filedialog
from dark_title_bar import * # Importação do código para aparencia da janela (fonte: https://gist.github.com/Olikonsti/879edbf69b801d8519bf25e804cec0aa )

tarefas = []  # Lista para armazenar as tarefas

class EstiloBotao(tk.Button): # Classe que irá personalizar todos os botões do menu inicial que por si mesma leva como atributo a classe Button implementada pelo Tkinter
     def __init__(self, master, text, command): # Método construtor, definindo master como widget Pai
        super().__init__(master, text=text, command=command) # A função chama o método construtor da classe
        self.config(bg="black", activebackground="dodgerblue1", width=14, height=2, font=("Cascadia Mono", 10), fg="white")
        self.pack(pady=5)

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = acao.get() # Extração do input do widget "acao"
    if tarefa:
        tarefas.append(tarefa) # Utilização do método append para adicionar a tarefa inserida á lista
        acao.delete(0, tk.END) # Limpeza do widget depois da extração do input
        messagebox.showinfo("", "Tarefa adicionada.")
        janela_adicionar.destroy() # Destruição da janela 
    else:
        messagebox.showerror("Erro", "Não inseriu nenhuma tarefa. \nPor favor, tente outra vez.")

# Função para excluir a tarefa selecionada da lista
def excluir_tarefa():
    indice_tarefa_selecionada = lista_tarefas.curselection() # Método do tinker para devolver um tuple com os indices selecionados
    if indice_tarefa_selecionada: # Condição para verificar se alguma tarefa foi selecionada
        tarefas.pop(indice_tarefa_selecionada[0]) # Utilização do método "pop" do Tinker para remoção da tarefa do index
        messagebox.showinfo("", "Tarefa excluida.")
        janela_excluir.destroy() # Destruição da janela
    else:
        messagebox.showerror("Erro", "Não selecionou nenhuma tarefa. \nPor favor, tente outra vez.")

# Função para visualizar todas as tarefas numa nova janela e personalização da mesm
def visualizar_tarefas():
    janela_visualizar = tk.Toplevel(root) # Criação de uma nova janela independente
    dark_title_bar(janela_visualizar)
    janela_visualizar.mainloop
    janela_visualizar.title("Lista de Tarefas")
    janela_visualizar.geometry("300x300")
    janela_visualizar.config(bg="dodgerblue4")

    titulo_tarefas = tk.Label(janela_visualizar, text="Lista de Tarefas", font=("Berlin Sans Fb", 20), bg="dodgerblue4")
    titulo_tarefas.pack(pady=10)

    texto_tarefas = tk.Text(janela_visualizar, height=10, width=30)
    texto_tarefas.pack(pady=10)

    for tarefa in tarefas: # Ciclo para inserção de cada tarefa no widget da janela de visualização
        texto_tarefas.insert(tk.END, tarefa + "\n")

# Função para abrir a janela Adicionar Tarefa
def abrir_janela_adicionar():
    global janela_adicionar
    janela_adicionar = tk.Toplevel(root) # Criação de uma nova janela independente
    dark_title_bar(janela_adicionar)
    janela_adicionar.mainloop
    janela_adicionar.title("Adicionar Tarefa")
    janela_adicionar.geometry("300x300")
    janela_adicionar.config(bg="dodgerblue4")

    titulo_adicionar = tk.Label(janela_adicionar, text="Adicionar Tarefa", font=("Berlin Sans Fb", 20), bg="dodgerblue4")
    titulo_adicionar.pack(pady=10)

    global acao # Definição da variável como global
    acao = tk.Entry(janela_adicionar, width=40) # Atribuição da variável a um widget e definição dos seus atributos
    acao.pack(pady=10)

    botao_adicionar = tk.Button(janela_adicionar, text="Adicionar Tarefa", command=adicionar_tarefa)
    botao_adicionar.config(bg="black", activebackground="dodgerblue1", width=20, height=2, font=("Cascadia Mono", 10), fg="white")
    botao_adicionar.pack(pady=5)

# Função para abrir a janela Excluir Tarefa
def abrir_janela_excluir():
    global janela_excluir
    janela_excluir = tk.Toplevel(root)
    dark_title_bar(janela_excluir)
    janela_excluir.mainloop
    janela_excluir.title("Excluir Tarefa")
    janela_excluir.geometry("300x300")
    janela_excluir.config(bg="dodgerblue4")

    titulo_excluir = tk.Label(janela_excluir, text="Selecione a tarefa a excluir", font=("Berlin Sans Fb", 16), bg="dodgerblue4")
    titulo_excluir.pack(pady=10)

    global lista_tarefas # Definição de uma variável globall
    lista_tarefas = tk.Listbox(janela_excluir, selectmode=tk.SINGLE, height=10, width=40) # Atribuição da variável a classe ListBox com os seus atributos
    lista_tarefas.pack(pady=10)

    for tarefa in tarefas:
        lista_tarefas.insert(tk.END, tarefa)

    botao_excluir = tk.Button(janela_excluir, text="Excluir Tarefa", command=excluir_tarefa)
    botao_excluir.config(bg="black", activebackground="dodgerblue1", width=14, height=2, font=("Cascadia Mono", 10), fg="white")
    botao_excluir.pack(pady=5)

# Função para exportar a lista para um arquivo CSV
def exportar_csv():
    if not tarefas:
        messagebox.showwarning("Aviso", "A lista de tarefas está vazia.")
        return

    df = pd.DataFrame(tarefas, columns=["Tarefa"])
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("", f"A lista de tarefas foi exportada para:\n{file_path}")

# Função para importar a lista de um arquivo CSV
def importar_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        try:
            df = pd.read_csv(file_path)
            tarefas.extend(df["Tarefa"].tolist())
            messagebox.showinfo("", f"A lista de tarefas foi importada de:\n{file_path}")
        except pd.errors.EmptyDataError:
            messagebox.showwarning("Aviso", "O arquivo CSV está vazio.")
        except pd.errors.ParserError:
            messagebox.showerror("Erro", "Erro ao analisar o arquivo CSV.")

# Função principal
def main():
    # Criação a janela principal
    global root
    root = tk.Tk()
    dark_title_bar(root)
    root.mainloop
    root.title("Lista de Tarefas")
    root.geometry("400x400")
    root.config(bg="dodgerblue4")

    menu_titulo = tk.Label(root, text="Lista de Tarefas", font=("Berlin Sans Fb", 20), bg="dodgerblue4")
    menu_titulo.pack(pady=10)

    # A função main instancia os atributos da classe EstiloBotao
    botao_adicionar = EstiloBotao(root, "Adicionar", abrir_janela_adicionar)
    botao_excluir = EstiloBotao(root, "Excluir", abrir_janela_excluir)
    botao_visualizar = EstiloBotao(root, "Visualizar", visualizar_tarefas)
    botao_exportar_csv = EstiloBotao(root, "Exportar CSV", exportar_csv)
    botao_importar_csv = EstiloBotao(root, "Importar CSV", importar_csv)

    botao_adicionar.pack(pady=5)
    botao_excluir.pack(pady=5)
    botao_visualizar.pack(pady=5)
    botao_exportar_csv.pack(pady=5)
    botao_importar_csv.pack(pady=5)

    root.mainloop()
# Invocação da função main
if __name__ == "__main__":
    main()
