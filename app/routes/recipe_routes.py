import json


from flask import Blueprint, jsonify




def create_blueprint(service):
    bp = Blueprint('recipe_bp', __name__)

    @bp.route('/', methods=['GET'])
    def get_recipes():
        """
        Get all recipes
        ---
        tags:
          - Recipes
        responses:
          200:
            description: List of all recipes
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
          500:
            description: Internal server error
        """
        try:
            data = service._repository.get_recipes()
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    

    @bp.route('/<recipe_id>', methods=['GET'])
    def get_recipes_by_id(recipe_id):
        """
        Get a recipe by ID
        ---
        tags:
          - Recipes
        parameters:
          - name: recipe_id
            in: path
            type: string
            required: true
            description: ID of the recipe to retrieve
        responses:
          200:
            description: Recipe data
            content:
              application/json:
                schema:
                  type: object
          404:
            description: Recipe not found
          500:
            description: Internal server error
        """
        try:
            data = service._repository.get_recipe_by_id(recipe_id)
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return bp