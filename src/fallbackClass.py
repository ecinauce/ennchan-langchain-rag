class FallbackLoader:
    def load(primary_loader, fallback_loader):
        if primary_loader is not None:
            if isinstance(primary_loader, str) and primary_loader in ["0", "1"]:
                return bool(int(primary_loader))
            elif isinstance(primary_loader, int):
                return bool(primary_loader)
            return primary_loader
        else:
            print("Primary loader failed, trying fallback loader...")
            return fallback_loader