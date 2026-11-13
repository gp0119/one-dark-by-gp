// 在 resources 中修改主题并保存，观察界面和这段代码的配色。
interface ThemePreview {
  name: string;
  colors: string[];
  enabled: boolean;
}

const theme: ThemePreview = {
  name: 'One Dark by GP',
  colors: ['#3C444E', '#ABB2BF', '#568AF2'],
  enabled: true,
};

export function describeTheme({ name, colors, enabled }: ThemePreview): string {
  const count = colors.filter(color => /^#[\da-f]{6}$/i.test(color)).length;
  return `${name}: ${count} colors, ${enabled ? 'enabled' : 'disabled'}`;
}

console.log(describeTheme(theme));
