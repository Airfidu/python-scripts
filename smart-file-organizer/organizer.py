import os
import shutil
from datetime import datetime
from pathlib import Path

class FileOrganizer:
    """Professional File Organizer - Organizes files by type and date"""
    
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        
        # File categories
        self.categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'Programming': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.json', '.xml'],
            'Applications': ['.exe', '.msi', '.apk', '.dmg', '.deb', '.rpm'],
            'Others': []
        }
        
        self.stats = {
            'total_files': 0,
            'organized_files': 0,
            'skipped_files': 0,
            'errors': 0
        }
    
    def get_category(self, file_ext):
        """Determines file category based on extension"""
        file_ext = file_ext.lower()
        for category, extensions in self.categories.items():
            if file_ext in extensions:
                return category
        return 'Others'
    
    def get_file_date(self, file_path):
        """Extracts file creation or modification date"""
        try:
            timestamp = os.path.getmtime(file_path)
            return datetime.fromtimestamp(timestamp)
        except:
            return datetime.now()
    
    def create_safe_filename(self, dest_path, filename):
        """Creates a safe filename in case a file with the same name exists"""
        if not dest_path.exists():
            return dest_path
        
        base_name = dest_path.stem
        extension = dest_path.suffix
        counter = 1
        
        while dest_path.exists():
            new_name = f"{base_name}_{counter}{extension}"
            dest_path = dest_path.parent / new_name
            counter += 1
        
        return dest_path
    
    def organize_files(self, by_date=True, by_type=True):
        """Organizes files in the specified folder"""
        
        if not self.source_dir.exists():
            print(f"❌ Folder does not exist: {self.source_dir}")
            return
        
        print(f"🚀 Starting file organization in: {self.source_dir}")
        print("=" * 60)
        
        # Read all files
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        self.stats['total_files'] = len(files)
        
        if not files:
            print("📭 No files to organize")
            return
        
        for file_path in files:
            try:
                # Skip hidden files
                if file_path.name.startswith('.'):
                    self.stats['skipped_files'] += 1
                    continue
                
                # Get file information
                file_name = file_path.name
                file_ext = file_path.suffix
                file_date = self.get_file_date(file_path)
                category = self.get_category(file_ext)
                
                # Build new path
                dest_parts = [self.source_dir]
                
                if by_type:
                    dest_parts.append(category)
                
                if by_date:
                    year = str(file_date.year)
                    month = f"{file_date.month:02d}-{file_date.strftime('%B')}"
                    dest_parts.extend([year, month])
                
                dest_dir = Path(*dest_parts)
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                # Move file
                dest_path = dest_dir / file_name
                dest_path = self.create_safe_filename(dest_path, file_name)
                
                shutil.move(str(file_path), str(dest_path))
                
                print(f"✅ Moved: {file_name}")
                print(f"   → To: {dest_path.relative_to(self.source_dir)}")
                
                self.stats['organized_files'] += 1
                
            except Exception as e:
                print(f"❌ Error processing {file_path.name}: {str(e)}")
                self.stats['errors'] += 1
        
        # Print statistics
        self.print_statistics()
    
    def print_statistics(self):
        """Prints organization statistics"""
        print("\n" + "=" * 60)
        print("📊 Organization Statistics:")
        print("=" * 60)
        print(f"📁 Total files: {self.stats['total_files']}")
        print(f"✅ Organized files: {self.stats['organized_files']}")
        print(f"⏭️  Skipped files: {self.stats['skipped_files']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print("=" * 60)
        
        if self.stats['organized_files'] > 0:
            success_rate = (self.stats['organized_files'] / self.stats['total_files']) * 100
            print(f"🎯 Success rate: {success_rate:.1f}%")
        
        print("\n✨ Organization completed successfully!")


def main():
    """Main function to run the script"""
    
    print("=" * 60)
    print("🗂️  Professional File Organizer")
    print("=" * 60)
    print()
    
    # Ask user for path input
    print("📂 Enter the folder path to organize:")
    print("   (or press Enter to use current folder)")
    
    source = input("Path: ").strip()
    
    if not source:
        source = os.getcwd()
    
    # Organization options
    print("\n⚙️  Organization options:")
    print("1. Organize by type only")
    print("2. Organize by date only")
    print("3. Organize by type and date (recommended)")
    
    choice = input("\nChoose method (1-3) [default: 3]: ").strip()
    
    by_type = choice in ['1', '3', '']
    by_date = choice in ['2', '3', '']
    
    # Confirm organization
    print(f"\n⚠️  Files will be organized in: {source}")
    confirm = input("Do you want to continue? (yes/no) [yes]: ").strip().lower()
    
    if confirm not in ['yes', 'y', '']:
        print("❌ Cancelled")
        return
    
    # Execute organization
    organizer = FileOrganizer(source)
    organizer.organize_files(by_date=by_date, by_type=by_type)


if __name__ == "__main__":
    main()