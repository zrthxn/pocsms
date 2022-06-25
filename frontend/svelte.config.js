import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';
import path from 'path';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess(),

	kit: {
		adapter: adapter(),
		prerender: {
			default: true,
		},
		vite: {
			resolve: {
				alias: {
					$comp: path.resolve('src/components'),
					$lib: path.resolve('src/lib'),
				}
			}
		}
	}
};

export default config;
