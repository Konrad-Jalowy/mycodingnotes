const AppConfig = (function() {
    let instance;
    let config = {};

    function createInstance(initialConfig) {
        config = initialConfig;
        return {
            getConfig: function() {
                return config;
            },
            updateConfig: function(newConfig) {
                config = {...config, ...newConfig};
            }
        }
    }

    return {
        getInstance: function(initialConfig) {
            if (!instance) {
                instance = createInstance(initialConfig);
            }

            return instance;
        }
    };
})();