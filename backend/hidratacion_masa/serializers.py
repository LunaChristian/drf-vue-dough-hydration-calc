from rest_framework import serializers

class HidratacionMasaSerializer(serializers.Serializer):
    cantidad_harina = serializers.DecimalField(
        max_digits=6, 
        decimal_places=2,
        min_value=0.1,
        help_text="Cantidad de harina en gramos"
    )
    cantidad_agua = serializers.DecimalField(
        max_digits=6, 
        decimal_places=2,
        min_value=0.1,
        help_text="Cantidad de harina en gramos"
    )

    def validate(self, data):
        """
        Validaciones personalizadas a nivel de objeto
        """
        harina = data.get('cantidad_harina')
        agua = data.get('cantidad_agua')
        
        # Regla de negocio 1: El agua no puede ser mayor que la harina
        if agua > harina:
            raise serializers.ValidationError({
                'agua': 'El agua no puede ser mayor que la cantidad de harina'
            })
        
        # Regla de negocio 2: Hidratación mínima del 50%
        hidratacion = (agua / harina) * 100
        if hidratacion < 50:
            raise serializers.ValidationError({
                'agua': f'Hidratación muy baja ({hidratacion:.1f}%). Mínimo recomendado: 50%'
            })
        
        # Regla de negocio 3: Hidratación máxima del 80%
        if hidratacion > 80:
            raise serializers.ValidationError({
                'agua': f'Hidratación muy alta ({hidratacion:.1f}%). Máximo recomendado: 80%'
            })
        
        return data