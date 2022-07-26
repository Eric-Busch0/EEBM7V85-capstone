function a = shell_run(data)
model = load('model.mat');

[a, throwaway] = predict(model.model, data);

end