from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class google_drive():
	def __init__(self, defaul_folder_id=""):
		""" folder_id est l'id du dossier (peut-être trouvé dans l'url) par ex. 1lOU_H78rPJr8eg6eXkc1ZuvfD6cZ-sLW """
		self.gauth = GoogleAuth()           
		self.drive = GoogleDrive(self.gauth)
		self.defaul_folder_id = defaul_folder_id

	def upload_file(self, filepath, folder_id="", filename="", shared=False):
		""" uploader un fichier
			
			Renvoie l'id du fichier et le lien de partage
		"""
		if folder_id == "" and self.defaul_folder_id != "":
			folder_id = self.defaul_folder_id
		else:
			raise ValueError("Aucun dossier de travail spécifié")

		metadata = {'parents': [{'id': folder_id}]}
		if filename != "":
			metadata["title"] = filename
		file = self.drive.CreateFile(metadata)
		file.SetContentFile(filepath)
		file.Upload()
		if shared:
			permission = file.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})
		return file["id"], file['alternateLink']

	def delete(self, file_id, folder_id=""):
		""" Suppression d'un fichier """

		if folder_id == "" and self.defaul_folder_id != "":
			folder_id = self.defaul_folder_id
		else:
			raise ValueError("Aucun dossier de travail spécifié")

		metadata = {'id': file_id}
		file = self.drive.CreateFile(metadata)
		file.Upload()
		file.Delete()