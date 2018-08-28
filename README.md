freecad-ng300-case
==================
**Короб с десятью аккумуляторами**
----------------------------------
                          
Данный код предосталяет возможность пользователю создать короб с десятью аккумуляторами (в нашем случаи используется для постраяния короба с десятью аккумуляторами ТНЖ-300ВМП-У2).


Габаритные размеры кробоа будут получены автоматически: они имеют зависимость от параметров, который вводит пользователь и параметры, которые имеет код по умолчани. Габариты аккумуляторов вводятся ползьзователем (batteryWidth, batteryDepth, batteryHeight). При построении стенок короба от их высоты вычитается 150 мм по умолчанию.

Короб будет собран из дривесно-стружечной плиты (ДСП). ДСП имеет следующие параметры:
1. Марка ДСП. Существуют две марки ДСП: П-А и П-Б. Эти марки различаются своими физико-механическими характеристиками. Марка П-А более высокого качества и имеет перед маркой П-Б лучшие показатели прочности на изгиб и растяжение и более низкие показатели по проценту разбухания, покоробленности и шероховатости поверхности.
2. Сорт ДСП. Различают плиты 1 сорта, 2 сорта, а также несортную плиту, используемую, как правило, в строительных целях. Основные различия между 1 и 2 сортом:
> - на плите первого сорта не допускаются выступы или углубления, смоляные или парафиновые пятна;
> - на плите первого сорта не допускаются сколы кромок и выкрашивание углов (исключение - единичные сколы (выкрашивание) до 3 мм и протяженностью по кромке до 15 мм); на плите второго сорта допускаются сколы кромок в пределах отклонений по длине (ширине) плиты;
> - на поверхности плиты второго сорта могут быть дефекты шлифования (не более 10% от площади);
> - на поверхности плиты второго сорта могут в большей степени по сравнению с первым сортом присутствовать включения коры и крупной фракции стружки.
3. Вид наружного слоя ДСП. По типу наружного слоя различают плиты с мелкоструктурной поверхностью (М), обычной поверхностью и плиты с наружными слоями из крупной стружки. Последние используются только для строительных целей и под облицовку натуральным шпоном.
4. Обработка поверхности ДСП. Плиты бывают шлифованные (Ш) и нешлифованные.
5. Класс эмиссии формальдегида в ДСП. Класс эмиссии показывает допустимое ГОСТ 10632-89 содержание свободного формальдегида в 100 граммах абсолютно сухой плиты. Существуют два класса эмиссии: Е1 (до 10 мг), Е2 (10-30 мг). Изготовление плиты с большим содержанием формальдегида недопустимо.
6. Водостойкость. Плиты бывают обычной и повышенной (буква «В» в маркировке) водостойкости. В подавляющем большинстве случаев используют плиты с обычной водостойкостью. Плиты повышенной водостойкости целесообразно использовать для изготовления столешниц для кухонь, мебели для ванных комнат, а также специальных строительных целей. При изготовлении водостойкой ДСП перед прессованием в стружечную массу вводят специальную парафиновую эмульсию или расплавленный парафин. Показателем водостойкости является разбухание по толщине (за 24 часа, верхний предел):
> - обычная ДСП, марка П-А - 22%,
> - обычная ДСП, марка П-Б - 33%,
> - водостойкая ДСП - не более 15%.
7. Огнестойкость. Для придания ДСП огнестойкости в ее состав вводят специальные вещества - антипирены.
8. Ламинирование ДСП. Это ДСП, облицованная пленкой на основе термореактивных полимеров (бумажно-смоляными пленками). 
На основе выше перечисленных параметров лист ДСП, необходимый нам, должен быть марки П-А,, 1-го сорта, с мелкострутурной поверхностью, шлифованным, с классом эмиссии Е-1, водостойкий (по возможности).
Это все будет иметь следующую маркировку: П-А, 1, М, Ш, Е1, В ...х...х18, ГОСТ 10632-89

Так же в коде заранее установлены такие параметры как: 
* расстояние между стенками коробо и батареями (row_betweenBattery); 
* толщина стенки короба (boxThickness);
* дополнительная высота к стенкам короба (additionalHeight);
* угол поворота короба в градусах (rotation); 
* поворот короба с аккумуляторами относительно оси x, y, z (x, y, z);
* маштабирования короба с аккумуляторами относительно оси x, y, z (scale_by_x, scale_by_y, scale_by_z).
Чертежи короба с десятью аккумуляторами ТНЖ-300ВМП-У2, а так же 3D модель короба представлены ниже на рисунках 1.1, 1.2, 1.3, 1.4 и 1.5.

![](https://github.com/solidiot/freecad-ng300-case/blob/master/Display%203D.png)

Рис. 1.1 – гланый вид чертежа короба для аккумулятора ТНЖ-300ВМП-У2

![](https://github.com/solidiot/freecad-ng300-case/blob/master/Display%20bottom%20side.png)

Рис. 1.2 –  передняя (задняя) стенка короба для аккумулятора ТНЖ-300ВМП-У2 

![](https://github.com/solidiot/freecad-ng300-case/blob/master/Display%20back%20side.png)                           

Рис. 1.3 –  левая (правая) боковая стенка короба для аккумулятора ТНЖ-300ВМП-У2

![](https://github.com/solidiot/freecad-ng300-case/blob/master/Display%20right%20side.png)

Рис. 1.4 –  нижняя стенка короба для аккумулятора ТНЖ-300ВМП-У2

![](https://github.com/solidiot/freecad-ng300-case/blob/master/ng300-10batteries-case.png)

Рис. 1.5 –  3D модель короба для аккумулятора ТНЖ-300ВМП-У2
