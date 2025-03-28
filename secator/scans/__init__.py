from secator.cli import ALL_SCANS


def generate_class(config):
	from secator.runners import Scan

	class scan(Scan):
		def __init__(self, inputs=[], **run_opts):
			hooks = run_opts.pop('hooks', {})
			results = run_opts.pop('results', [])
			context = run_opts.pop('context', {})
			super().__init__(
				config=config,
				inputs=inputs,
				results=results,
				run_opts=run_opts,
				hooks=hooks,
				context=context)
	return scan, config.name


DYNAMIC_SCANS = {}
for scan in ALL_SCANS:
	cls, name = generate_class(scan)
	DYNAMIC_SCANS[name] = cls

globals().update(DYNAMIC_SCANS)
__all__ = list(DYNAMIC_SCANS)
