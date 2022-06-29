# Generated by Django 4.0.4 on 2022-06-28 23:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_Categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID CATEGORIA:')),
                ('categoria', models.CharField(max_length=25, verbose_name='CATEGORIA: ')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='RUT: ')),
                ('nombre', models.CharField(max_length=50, verbose_name='NOMBRE: ')),
                ('telefono', models.CharField(max_length=12, verbose_name='TELEFONO: ')),
                ('correo', models.EmailField(max_length=80, verbose_name='CORREO ELECTRONICO: ')),
                ('suscripcion', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombreComuna', models.CharField(max_length=20, verbose_name='NOMBRE COMUNA: ')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idcontacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, verbose_name='NOMBRE: ')),
                ('email', models.CharField(max_length=35, verbose_name='EMAIL: ')),
                ('consulta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('idDespacho', models.AutoField(primary_key=True, serialize=False)),
                ('nombreDespacho', models.CharField(max_length=25, verbose_name='NOMBRE RECEPTOR: ')),
                ('direccionDespacho', models.CharField(max_length=25, verbose_name='DIRECCIÓN DESPACHO: ')),
                ('telefono', models.CharField(max_length=25)),
                ('nombreComuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nombre_comuna', to='core.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idpedido', models.AutoField(primary_key=True, serialize=False)),
                ('forma_pago', models.BooleanField(verbose_name='FORMA PAGO: ')),
                ('estado_pedido', models.CharField(max_length=25, verbose_name='ESTADO PEDIDO: ')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('cantidad', models.IntegerField(verbose_name='CANTIDAD: ')),
                ('valor_total', models.IntegerField(verbose_name='VALOR TOTAL: ')),
                ('direccionDespacho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='direccion_despacho', to='core.despacho')),
                ('nombreComuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nombre_comuna_p', to='core.comuna')),
                ('nombreDespacho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nombre_despacho', to='core.despacho')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRegion', models.CharField(max_length=20, verbose_name='NOMBRE REGION: ')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('idSubcategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID SUBCATEGORIA:')),
                ('subCategoria', models.CharField(max_length=50, verbose_name='SUBCATEGORIA: ')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='USUARIO: ')),
                ('contrasenia', models.CharField(max_length=15, verbose_name='CONTRASENIA: ')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fecha_ven', to='core.pedido')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedido_ven', to='core.pedido')),
                ('valortotal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valor_total_ven', to='core.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID PRODUCTO:')),
                ('nombre_producto', models.CharField(max_length=30, verbose_name='NOMBRE PRODUCTO: ')),
                ('descripcion', models.TextField(max_length=200, verbose_name='DESCRIPCION: ')),
                ('valor', models.IntegerField(verbose_name='VALOR: ')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('valor_oferta', models.IntegerField(blank=True, null=True, verbose_name='VALOR OFERTA: ')),
                ('oferta', models.BooleanField(max_length=10, verbose_name='OFERTA: ')),
                ('stock', models.IntegerField(verbose_name='STOCK: ')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categoria_produ', to='core.categoria')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcate_produ', to='core.subcategoria')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombreRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nombre_region', to='core.region'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='core.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='telefono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tel', to='core.despacho'),
        ),
        migrations.AddField(
            model_name='despacho',
            name='nombreRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nombre_region_d', to='core.region'),
        ),
    ]